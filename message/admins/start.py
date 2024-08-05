from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import data
import keyboards

async def start(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum, admin!", reply_markup=keyboards.reply.admin_menu)
    