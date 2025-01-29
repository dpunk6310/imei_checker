import httpx

from .config import IMEI_API_TOKEN


async def check_imei_device(device_id: str):
    url = "https://api.imeicheck.net/v1/checks"

    headers = {
        "Authorization": f"Bearer {IMEI_API_TOKEN}",
        "Content-Type": "application/json"
    }

    body = {
        "deviceId": device_id,
        "serviceId": 12
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            data.pop("!!! WARNING !!!")
            return data
        except httpx.HTTPStatusError as err:
            return {"error": f"HTTP error {err.response.status_code}: {err.response.text}"}
        except httpx.RequestError as err:
            return {"error": f"Request error: {str(err)}"}
        except Exception as err:
            return {"error": f"Unexpected error: {str(err)}"}