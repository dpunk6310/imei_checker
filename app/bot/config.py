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


def get_admins_tg():
    return ADMINS.split(",")
