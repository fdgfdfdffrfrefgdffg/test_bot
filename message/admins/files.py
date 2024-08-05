from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from asyncio import sleep
import data
import keyboards
import states

async def get_files(message: Message, state: FSMContext):
    fayllar = data.get_files()
    if fayllar:
        await message.answer("❗ Iltimos, fayllarni yuborib bo'lishimni kuting. Yuborib bo'lganimda xabar qilaman.", reply_markup=ReplyKeyboardRemove())
        for fayl in fayllar:
            await message.answer_document(
                fayl[1],
                caption="" + fayl[2],
                reply_markup=keyboards.inline.del_fayl_btn(fayl[0])
            )
            sleep(1)
        await message.answer("❗ Fayllarni yuborib bo'ldim", reply_markup=keyboards.reply.files_menu)
    else:
        await message.answer("❗ Bazaga hali fayllar qo'shilmagan!", reply_markup=keyboards.reply.files_menu)

async def add_file_answer(message: Message, state: FSMContext):
    await message.answer("Fayl yuborishingiz mumkin.", reply_markup=keyboards.reply.cancel_menu)
    await state.set_state(states.admins.AddFileState.file)

async def add_file_file_answer(message: Message, bot: Bot, state :FSMContext):
    if not message.document:
        await message.answer("Menga fayl yuboring.", reply_markup=keyboards.reply.cancel_menu)
        return
    data.add_file(
        message.document.file_id,
        message.document.file_name
    )
    await bot.send_document(
        chat_id=-1002202845242,
        document=message.document.file_id,
        caption=message.document.file_name
    )
    await state.clear()
    await message.answer("✅ Fayl saqlandi!", reply_markup=keyboards.reply.files_menu)
