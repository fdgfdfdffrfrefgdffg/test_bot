from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from asyncio import sleep
from datetime import timedelta
from time import time
import data, keyboards, states


async def start_vik_answer(call: CallbackQuery, state: FSMContext):
    vik_id = call.data.split(":")[1]
    tests = data.get_quizs_vik(vik_id)
    print(tests)
    if tests:
        test = tests[0]
        await call.answer("✅ Test boshlandi!")
        options = [i for i in [test[2], test[3], test[4], test[5], test[6], test[7]] if i]

        await call.message.answer_poll(
                    question=test[1],
                    options=options,
                    type="quiz",
                    correct_option_id=test[8],
                    is_anonymous=False,
                    close_date=timedelta(minutes=4, seconds=0),
                    reply_markup=keyboards.inline.next_test_btn
                )
        tests.remove(test)
        if tests: await state.update_data(tests=tests, correct_id=test[8], t=0, vik_id=vik_id, s_time=time(), tugadi=True)
        await state.set_state(states.users.StatrtTest.quiz)

    else:
        await call.answer("Bu testga hali savollar qo'shilmagan")
        await call.message.answer("Asosiy menyudasiz!", reply_markup=keyboards.reply.user_menu)
    await call.message.delete()

async def next_test_answer(call: CallbackQuery, state: FSMContext):
    context_data = await state.get_data()
    tests = context_data.get("tests")
    
    if tests:
        test = tests[0]
        options = [i for i in [test[2], test[3], test[4], test[5], test[6], test[7]] if i]

        await call.message.answer_poll(
                    question=test[1],
                    options=options,
                    type="quiz",
                    correct_option_id=test[8],
                    is_anonymous=False,
                    close_date=timedelta(minutes=4, seconds=0),
                    reply_markup=keyboards.inline.next_test_btn
                )
        tests.remove(test)
        await state.update_data(tests=tests, correct_id=test[8])
        await state.set_state(states.users.StatrtTest.quiz)
    else:
        context_data = await state.get_data()
        t = context_data.get("t")
        vik_id = context_data.get("vik_id")
        len_quizs = len(data.get_quizs_vik(vik_id))
        s_time = context_data.get("s_time")
        save_time = time() - s_time
        vaqt = ""
        vaqt += str(int(save_time // 3600)).zfill(2) + ":"
        vaqt += str(int(save_time % 3600 // 60)).zfill(2) + ":"
        vaqt += str(int(save_time % 3600 % 60)).zfill(2)
        
        await call.message.answer(
            text=f"TEST TUGADI!\n\n❓ Savollar soni: {len_quizs} ta\n✅ To'g'ri javoblar: {t} ta\n⏰ Sarflangan vaqt: {vaqt}",
            reply_markup=keyboards.reply.user_menu
        )
        s_time = context_data.get("s_time")
        vaqt = time() - s_time
        
        data.add_result(
            call.from_user.id,
            vik_id,
            t,
            save_time
        )
        await state.clear()
    await call.answer()

async def end_test_next_test_answer(call: CallbackQuery):
    await call.answer("❗ Ushbu test tugagan!", show_alert=True)
    await call.message.delete()
