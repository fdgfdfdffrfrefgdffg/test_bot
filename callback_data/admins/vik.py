from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
import data
import states
import keyboards

async def get_vik_answer(call: CallbackQuery, state: FSMContext):
    vik_id = call.data.split(":")[1]
    tests = data.get_quizs_vik(vik_id)
    await state.update_data(id=vik_id)
    print(tests)
    if tests:
        await call.message.answer("❓ Savollarni yuborib bo'lishimni kuting", reply_markup=ReplyKeyboardRemove())
        for test in tests:
            options = [i for i in [test[2], test[3], test[4], test[5], test[6], test[7]] if i]

            await call.message.answer_poll(
                question=test[1],
                options=options,
                type="quiz",
                correct_option_id=test[8],
                is_anonymous=False,
                reply_markup=keyboards.inline.del_quiz_btn(test[0])
            )
        await call.message.answer("✅ Testlarni yuborib bo'ldim!", reply_markup=keyboards.reply.vik_menu_admin)
    else:
        await call.message.answer("❗ Bu viktorinada savollar mavjud emas", reply_markup=keyboards.reply.vik_menu_admin)
    await call.answer()
    await call.message.delete()







async def del_quiz_answer(call: CallbackQuery):
    quiz_id = int(call.data.split(":")[1])
    data.del_quiz(quiz_id)
    await call.answer("✅ Test o'chirildi!", show_alert=True)
    await call.message.delete()

async def del_vik_answer(call: CallbackQuery):
    vik_id = int(call.data.split(":")[1])
    data.del_quiz(vik_id)
    data.del_quizs_vik(vik_id)
    await call.answer("✅ Viktorina o'chirildi!", show_alert=True)
    await call.message.delete()
