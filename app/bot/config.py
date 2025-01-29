import os

from dotenv import load_dotenv


dotenv_path = '.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print("Not .env file")
    exit(1)


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS")
IMEI_API_TOKEN = os.getenv("IMEI_API_TOKEN")
BACKEND_DOMAIN = os.getenv("BACKEND_DOMAIN")


def get_admins_tg():
    return ADMINS.split(",")
