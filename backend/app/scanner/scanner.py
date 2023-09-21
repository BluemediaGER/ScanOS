import gi, os, threading
from typing import List

from PIL import Image
from app.scanner.enums import Status

gi.require_version('Libinsane', '1.0')
from gi.repository import Libinsane, GObject # type: ignore

class __LibinsaneSilentLogger(GObject.GObject, Libinsane.Logger):
    def do_log(self, lvl, msg):
        return
    
Libinsane.register_logger(__LibinsaneSilentLogger())

class Page:
    filename: str
    size_bytes: int

class Scanner:

    def __get_device_id(self):
        """
        List local scanners and get the device id of the first found device.

        :param self: Instance of this class
        :returns: Device id of the first scan device
        """
        devs = self.api.list_devices(Libinsane.DeviceLocations.LOCAL_ONLY)
        return devs[0].get_dev_id()

    def __raw_to_img(self, params, img_bytes):
        """
        
        """
        fmt = params.get_format()
        assert(fmt == Libinsane.ImgFormat.RAW_RGB_24)
        (w, h) = (
            params.get_width(),
            int(len(img_bytes) / 3 / params.get_width())
        )
        return Image.frombuffer("RGB", (w, h), img_bytes, "raw", "RGB", 0, 1)

    def __write_file(self, scan_params, data, page_index, last_file):
        data = b"".join(data)
        if scan_params.get_format() == Libinsane.ImgFormat.RAW_RGB_24:
            filesize = len(data)
            img = self.__raw_to_img(scan_params, data)
            filename = f"out{page_index}.png"
            img.save(os.path.join(self.storage_path, filename), format="PNG")
            page = Page()
            page.filename = filename
            page.size_bytes = filesize
            self.scanned_pages.append(page)
        if last_file:
            self.status = Status.DONE

    def __set_defaults(self):
        dev = self.api.get_device(self.device_id)
        opts = dev.get_options()
        opts = {opt.get_name(): opt for opt in opts}
        opts["sleeptimer"].set_value(1)
        opts["resolution"].set_value(200)
        dev.close()

    def __scan(self):
        self.status = Status.RUNNING
        source = self.api.get_device(self.device_id)

        opts = source.get_options()
        opts = {opt.get_name(): opt for opt in opts}
        if opts["cover-open"].get_value() == True:
            self.status = Status.ERR_COVER_OPEN
            return
        
        session = source.scan_start()
        try:
            page_index = 0
            while not session.end_of_feed() and page_index < 50:
                # Do not assume that all the pages will have the same size !
                scan_params = session.get_scan_parameters()
                img = []
                while not session.end_of_page():
                    data = session.read_bytes(256 * 1024)
                    data = data.get_data()
                    img.append(data)
                t = threading.Thread(target=self.__write_file, args=(scan_params, img, page_index, session.end_of_feed()))
                t.start()
                page_index += 1
            if page_index == 0:
                self.status = Status.ERR_NO_PAPER
        finally:
            session.cancel()
            source.close()
    
    def __init__(self, storage_path):
        self.scanned_pages: List[Page] = []
        self.storage_path = storage_path
        self.status = Status.INITIALIZED

    def preload(self):
        os.environ["LIBINSANE_NORMALIZER_SAFE_DEFAULTS"] = "0"
        self.api = Libinsane.Api.new_safebet()
        self.device_id = self.__get_device_id()
        self.__set_defaults()
        self.status = Status.IDLE

    def scan(self):
        if self.status == Status.RUNNING:
            raise RuntimeError("already_running")
        if self.status == Status.INITIALIZED:
            self.preload()
        self.scanned_pages: List[Page] = []
        t = threading.Thread(target=self.__scan)
        t.start()

    def get_status(self) -> Status:
        return self.status
    
    def get_pages(self) -> List[Page]:
        return self.scanned_pages
    
    def get_options(self):
        dev = self.api.get_device(self.device_id)
        opts = dev.get_options()
        result = {}
        for opt in opts:
            try:
                result[opt.get_name()] = opt.get_value()
            except Exception:
                continue
        dev.close()
        return result
    
    def cleanup(self):
        if self.status == Status.RUNNING:
            raise RuntimeError("scan_running")
        if self.status != Status.INITIALIZED:
            self.api.cleanup()
    