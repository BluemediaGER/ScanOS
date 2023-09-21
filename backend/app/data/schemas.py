from pydantic import BaseModel
import app.scanner.enums as scan

class ScanPage(BaseModel):
    filename: str
    size_bytes: int

    class Config():
        orm_mode = True

class ScanStatus(BaseModel):
    pages: list[ScanPage]
    status: scan.Status