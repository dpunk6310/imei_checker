import asyncio

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from .utils import check_imei_device
from .auth import check_token


app = FastAPI(
    debug=True,
    title="IMEI Checker API",
)


class IMEIRequest(BaseModel):
    imei: str
    

@app.post("/api/check-imei", dependencies=[Depends(check_token)])
def check_imei(request: IMEIRequest):
    result = asyncio.run(check_imei_device(request.imei))
    if not result:
        raise HTTPException(status_code=404, detail="IMEI not found")
    return {"result": result}
