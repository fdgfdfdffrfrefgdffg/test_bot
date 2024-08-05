from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
import data, keyboards

async def get_stat_vik(message: Message):
    viks = data.get_viks_for_reyting(message.from_user.id)
    if viks:
        markup = keyboards.inline.get_viks_for_reyting_btn(viks)
        await message.answer("Testni tanlang.", reply_markup=markup)
    else:
        await message.answer("❗ Siz hali test yechmagansiz!", reply_markup=keyboards.reply.user_menu)
