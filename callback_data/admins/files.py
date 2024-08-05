from aiogram.types import CallbackQuery
import data

async def del_file_answer(call: CallbackQuery):
    file_id = int(call.data.split(":")[1])
    data.del_file(file_id)
    await call.answer("✅ Fayl o'chirildi1")
    await call.message.delete()
