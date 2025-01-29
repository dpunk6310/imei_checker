import os

from dotenv import load_dotenv


dotenv_path = '.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print("Not .env file")
    exit(1)


IMEI_API_TOKEN = os.getenv("IMEI_API_TOKEN")
