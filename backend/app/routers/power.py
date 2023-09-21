from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/api/power")

@router.post("/shutdown")
async def power_shutdown():
    subprocess.call(["sudo", "shutdown", "-h", "now"])
    return {}

@router.post("/restart")
async def power_restart():
    subprocess.call(["sudo", "reboot"])
    return {}