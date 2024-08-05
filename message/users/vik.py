from aiogram import Bot
from aiogram.types import Message, PollAnswer
from aiogram.fsm.context import FSMContext
from datetime import timedelta
from time import time
import data, keyboards, states


async def get_viks_answer(message: Message):
    viks = data.get_viks()
    if viks:
        markup = keyboards.inline.get_viks_btn(viks)
        await message.answer("❓ Viktorinalar", reply_markup=markup)
    else:
        await message.answer("❗ Viktorinalar topilmadi1", reply_markup=keyboards.reply.user_menu)

async def get_quiz_answer(poll: PollAnswer, bot: Bot, state: FSMContext):
    context_data = await state.get_data()
    if context_data.get("correct_id") in poll.option_ids:
        await state.update_data(t=context_data.get("t") + 1)
    tests = context_data.get("tests")
    
    if tests:
        test = tests[0]
        options = [i for i in [test[2], test[3], test[4], test[5], test[6], test[7]] if i]

        await bot.send_poll(
                    chat_id=poll.user.id,
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
        f = len(data.get_quizs_vik(vik_id)) - t
        s_time = context_data.get("s_time")
        save_time = time() - s_time
        vaqt = ""
        vaqt += str(int(save_time // 3600)).zfill(2) + ":"
        vaqt += str(int(save_time % 3600 // 60)).zfill(2) + ":"
        vaqt += str(int(save_time % 3600 % 60)).zfill(2)
        
        await bot.send_message(
            chat_id=poll.user.id,
            text=f"TEST TUGADI!\n\n✅ To'g'ri javoblar: {t} ta\n❌ Noto'g'ri javoblar: {f} ta\n⏰ Sarflangan vaqt: {vaqt}",
            reply_markup=keyboards.reply.user_menu
        )
        s_time = context_data.get("s_time")
        vaqt = time() - s_time
        
        data.add_result(
            poll.user.id,
            vik_id,
            t,
            save_time
        )
        await state.clear()
