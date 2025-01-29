from fastapi import HTTPException, Header

from .config import IMEI_API_TOKEN


def check_token(token: str = Header(...)) -> dict:
    if token != IMEI_API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
