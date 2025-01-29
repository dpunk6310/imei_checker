import httpx

from config import IMEI_API_TOKEN

async def check_imei_device(imei: str):
    url = "http://127.0.0.1:8000/api/check-imei"

    headers = {
        "Content-Type": "application/json",
        "token": IMEI_API_TOKEN
    }

    body = {
        "imei": imei
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            return data
        except httpx.HTTPStatusError as err:
            return {"error": f"HTTP error {err.response.status_code}: {err.response.text}"}
        except httpx.RequestError as err:
            return {"error": f"Request error: {str(err)}"}
        except Exception as err:
            return {"error": f"Unexpected error: {str(err)}"}
