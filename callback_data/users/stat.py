from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
import data, keyboards

async def get_stat_vik(call: CallbackQuery, state: FSMContext):
    vik_id = call.data.split(":")[1]
    reyting = data.get_results_test(vik_id)
    text = "TOP REYTING!\n\n"
    j = 0
    user_text = ""
    for i in reyting:
        user = data.get_user(i[0])
        if user:
            j += 1
            if j <= 10:
                vaqt = f"{int(i[3] // 3600):02}:{int(i[3] % 3600 // 60):02}:{int(i[3] % 3600 % 60):02}"
                text += f"{j}. {user.name}: {i[2]} ({vaqt})\n"
            if j > 10 and i[0] == call.from_user.id:
                user_text += f"\n{j}. {user.name}: {i[2]} ({vaqt})"
    text += user_text
    await call.message.answer(text)