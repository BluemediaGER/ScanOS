
<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/BluemediaGER/ScanOS/main/docs/img/logo.png" alt="ScanOS" width="300">
</h1>

<h4 align="center">A modern operating system for enterprise-grade network image scanners.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#supported-devices">Supported Devices</a> •
  <a href="#motivation">Motivation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a>
</p>

## Key Features

- [x] Modern UI design on top of a modern operating system (Debian 12)
- [x] Implemented fully using open-source components
- [ ] Scan to mail
- [ ] Scan to folder (SMB / FTP)
- [ ] Scan to Paperless-ngx
    - [ ] Editing of document properties right on the scanner (document type, correspondent, tags, etc.)
- [ ] OTA updates using RAUC
- [ ] Encrypted temporary storage for scanned files

## Supported devices

These devices are currently supported by ScanOS:
* Fujitsu N7100

## Motivation

I've recently bought a Fujitsu N7100 image scanner for cheap on eBay. The N7100 is basically a USB scanner combined with an Intel Atom x86 board, a SATA SSD, and a touchscreen. By default, it runs Windows 8 Embedded Standard and a lot of proprietary software. Windows 8 Embedded is EOL since April 2023 and receives no further updates. Additionally, writing custom extensions for the scanner's software to use its full potential is hard:
- You need the extension SDK, which is not easily accessible. EOL of the device made it even harder to acquire.
- Extensions are written in C# using .NET 4.5 and WPF
- The development process is quite ugly

So my idea was to try to get Linux running on this thing. Surprisingly, that task was really easy, as it's fairly standard hardware. Even the hardware scan button is just a USB keyboard with exactly one key: an enter key. The built-in scanner worked out of the box with SANE, so I started the development of a customized OS for use on the scanner.

## How To Use

ScanOS is currently in a very early development stage. There is no stable version or standardized development environment yet. Check back later for further usage instructions.

## Credits

ScanOS is built on top of many other great projects. Some of them are:

- [Debian 12 (Bookworm)](https://www.debian.org/)
- [Nginx](https://nginx.org/en/)
- [Sway](https://swaywm.org/)
- [Chromium](https://www.chromium.org/Home/)
- [debos - Debian OS images builder](https://github.com/go-debos/debos)
- [RAUC](https://rauc.io/)
- [Vue.js 3](https://vuejs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Libinsane](https://gitlab.gnome.org/World/OpenPaperwork/libinsane/-/tree/master)
- [FastAPI](https://fastapi.tiangolo.com/)

---

> [bluemedia.dev](https://bluemedia.dev) &nbsp;&middot;&nbsp;
> GitHub [@BluemediaGER](https://github.com/BluemediaGER) &nbsp;&middot;&nbsp;
> Mastodon [@Bluemedia@chaos.social](https://chaos.social/@Bluemedia)

