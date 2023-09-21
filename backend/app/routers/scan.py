from typing import Annotated

from app.scanner.scanner import Scanner
from app.main import get_scanner

from fastapi import APIRouter, Depends
from app.data import schemas, models

router = APIRouter(prefix="/api/scan")

@router.post("")
async def scan(scanner: Annotated[Scanner, Depends(get_scanner)]):
    scanner.scan()
    return []

@router.get("/status", response_model=schemas.ScanStatus)
async def status(scanner: Annotated[Scanner, Depends(get_scanner)]):
    pages = [schemas.ScanPage.from_orm(page) for page in scanner.get_pages()]
    return schemas.ScanStatus(pages=pages,status=scanner.get_status())

@router.get("/debug")
async def debug(scanner: Annotated[Scanner, Depends(get_scanner)]):
    return scanner.get_options()