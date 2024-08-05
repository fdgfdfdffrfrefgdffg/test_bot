from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
import keyboards.reply
import states
import keyboards
import data

async def start_db_user(message: Message):
    await message.answer("Asosiy menyudasiz!", reply_markup=keyboards.reply.user_menu)

async def start_not_user(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum, ism-familyangizni kiriting.", reply_markup=ReplyKeyboardRemove())
    await state.set_state(states.users.RegisterState.name)

async def answer_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Pastdagi tugmaga bosib telefon raqamingizni yuboring.", reply_markup=keyboards.reply.phone_menu)
    await state.set_state(states.users.RegisterState.phone)

async def answer_phone(message: Message, state: FSMContext):
    if not message.contact: 
        await message.answer("❗ Menga telefon raqamingizni yuborish uhun pastdagi tugmadan foydalaning.")
        return

    elif message.contact.user_id != message.from_user.id:
        await message.answer("❗ Menga o'zingizning telefon raqamingizni yuboring. Buning uchun pastdagi tugmadan foydalaning.") 
        return

    context = await state.get_data()
    data.add_user(
        message.from_user.id,
        context["name"],
        message.contact.phone_number
    )
    await message.answer("✅ Siz ro'yhatdan muvaffaqiyatli o'tdingiz!", reply_markup=keyboards.reply.user_menu)
    await state.clear()

