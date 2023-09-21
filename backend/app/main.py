import threading
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends

from app.data import models
from app.data.database import SessionLocal, engine

from app.scanner.scanner import Scanner
from app.scanner.scanner import Status as ScannerStatus

models.Base.metadata.create_all(bind=engine)

__scanner = Scanner("/var/www/html/img")

@asynccontextmanager
async def __lifespan(app: FastAPI):
    threading.Thread(target=__scanner.preload).start()
    yield

app = FastAPI(lifespan=__lifespan)

# SQLAlchemiy session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_scanner():
    return __scanner

from app.routers import power
app.include_router(power.router)

from app.routers import scan
app.include_router(scan.router)

@app.get("/api/ready")
async def __ready(scanner: Annotated[Scanner, Depends(get_scanner)]):
    return scanner.get_status() != ScannerStatus.INITIALIZED