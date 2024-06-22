import asyncio

from aiogram import Dispatcher, Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()
bot = Bot(token='6346623267:AAGjcGiTCK2UCj76uENqDfTJrGWNIYwUCXA')

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот, который поможет тебе с выбором маршрута')

async def start():
    dp.include_routers(router)

    await dp.start_polling(bot, )


asyncio.run(start())