from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards

async def cancel_answer(message: Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state: await state.clear()
    await message.answer("Amallar bekor qilindi! Bosh menyudasiz!", reply_markup=keyboards.reply.admin_menu)
    