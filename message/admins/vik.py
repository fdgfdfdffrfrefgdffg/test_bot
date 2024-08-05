from aiogram.types import Message
from aiogram.enums import PollType
from aiogram.fsm.context import FSMContext
import data
import keyboards
import states


async def get_viks(message: Message, state: FSMContext):
    viks = data.get_viks()
    if viks:
        markup = keyboards.inline.get_viks_btn(viks, admin=True)
        await message.answer("❓ Viktorinalar", reply_markup=markup)
    else:
        await message.answer("❗ Viktorinalar topilmadi1")
    await message.answer("Vikorina qo'shamizmi", reply_markup=keyboards.reply.viks_menu_admin)

async def add_vik_answer(message: Message, state: FSMContext):
    await message.answer("Viktorina nomini kiriting.")
    await state.set_state(states.admins.AddVikState.name)

async def add_vik_name_answer(message: Message, state: FSMContext):
    this_vik = data.add_vik(message.text)
    await state.update_data(id=this_vik[0])
    await message.answer("✅ Viktorina nomi saqlandi! Endi unga testlar qo'shamiz!", reply_markup=keyboards.reply.add_quiz_menu)
    await state.set_state(states.admins.AddQuiz.quiz)

async def add_vik_quiz_answer(message: Message, state: FSMContext):
    await message.answer("Endi mennga pastdagi tugma orqali testlar yuboring!", reply_markup=keyboards.reply.add_quiz_menu)
    await state.set_state(states.admins.AddQuiz.quiz)

async def add_quiz_answer(message: Message, state: FSMContext):
    if not message.poll: 
        await message.answer("Pastdagi tugma orqali test yaratib, menga yuboring.")
        return
    quiz = message.poll
    if quiz.type != PollType.QUIZ:
        await message.answer("Menga quiz (viktorina) yuboring.")
        return
    if quiz.correct_option_id:
        varinatlar = [None] * 6
        for index, value in enumerate(quiz.options):
            varinatlar[index] = value.text
        context = await state.get_data()
        data.add_quiz(
            vik_id=context.get("id"),
            question=quiz.question,
            tr_op=quiz.correct_option_id,
            op1=varinatlar[0],
            op2=varinatlar[1],
            op3=varinatlar[2],
            op4=varinatlar[3],
            op5=varinatlar[4],
            op6=varinatlar[5],
        )
        await message.answer(text="✅ Test bazaga saqlandi! Yana test yuborishingiz mumkin.", reply_markup=keyboards.reply.add_quiz_menu)
        await message.answer(text="Test yaratishni to'xtatish uchun 🚫 Bekor qilish tugmasidan foydalaning.")
    else: await message.answer("Iltimos, testni pastdagi tugma orqali yarating.", reply_markup=keyboards.reply.add_quiz_menu)
