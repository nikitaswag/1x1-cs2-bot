from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.commands import command_router
from handlers.states import fsm_router
from keyboards.reply import menu_keyboard
from handlers.callback import callbacks_router
from aiogram.fsm.storage.memory import MemoryStorage
from antiflood import AntiFloodMiddleware

storage = MemoryStorage()



from dotenv import load_dotenv
import os
import asyncio


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(callbacks_router)
dp.include_router(fsm_router)
dp.message.middleware(AntiFloodMiddleware())




async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
