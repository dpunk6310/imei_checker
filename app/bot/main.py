import asyncio
import logging
import sys
import json

from aiogram import Router
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message, ReplyKeyboardRemove

from bot import bot, dp
from config import get_admins_tg
from utils import is_valid_imei
from api import check_imei_device



form_router = Router()


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        admins = await get_admins_tg()
        if not admins:
            return False
        return message.from_user.id in admins


@form_router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, введи IMEI устройтва",
        reply_markup=ReplyKeyboardRemove(),
    )
    
    
@form_router.message()
async def all_msg_handler(message: Message) -> None:
    imei = message.text
    if not is_valid_imei(imei=imei):
        await message.answer(
            f"Невалидный IMEI",
            reply_markup=ReplyKeyboardRemove(),
        )
        return
    data = await check_imei_device(imei=imei)
    msg = f"<code>{json.dumps(data, indent=2, ensure_ascii=False)}</code>"
    await message.answer(msg, parse_mode="HTML")
        


async def main():
    dp.include_router(form_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
