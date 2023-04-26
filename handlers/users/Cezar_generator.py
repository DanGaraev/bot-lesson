from aiogram import types

from loader import dp
from utils import CezarGenerator

@dp.message_handler()
async def cz_generator(message: types.Message):
    cz = CezarGenerator(message.text)
    await message.answer(cz.cezar)
    return