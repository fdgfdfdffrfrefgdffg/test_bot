from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from asyncio import sleep
import data
import keyboards

async def select_category_answer(message: Message):
    await message.answer("Bo'limni tanlang.", reply_markup=keyboards.reply.choose_category)

async def get_files(message: Message):
    fayllar = data.get_files_category(message.text)
    if fayllar:
        await message.answer("❗ Iltimos, fayllarni yuborib bo'lishimni kuting. Yuborib bo'lganimda xabar qilaman.", reply_markup=ReplyKeyboardRemove())
        for fayl in fayllar:
            await message.answer_document(
                fayl[1],
                caption="" + fayl[2]
            )
            await sleep(1.5)
        await message.answer("❗ Fayllarni yuborib bo'ldim", reply_markup=keyboards.reply.user_menu)
    else:
        await message.answer("❗ Bazaga hali fayllar qo'shilmagan!", reply_markup=keyboards.reply.user_menu)
