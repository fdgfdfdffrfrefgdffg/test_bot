from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
import data, keyboards

async def get_stat_vik(message: Message, state: FSMContext):
    context_data = await state.get_data()
    if not context_data.get("id"):
        await message.answer("❗ Kerakli ma'lumotlar mavjud emas. Iltimos, qaytadan urinib ko'ring", reply_markup=keyboards.reply.user_menu)
        await state.clear()
        return
    reyting = data.get_results_test(context_data.get("id"))
    text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=sTATISTIKA, initial-scale=1.0">
    <title>Document</title>
    <style>
        table{
            width: 100%;
            border: 2px solid black;
        }
        thead {
            background-color: rgb(200, 90, 12);
            color: white;
        }
        tbody{
            background-color: rgb(245, 207, 179);
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>O'rin</th>
                <th>Ism-familya</th>
                <th>Telefon raqam</th>
                <th>Ball</th>
                <th>Vaqt</th>
            </tr>
        </thead>
        <tbody>
"""

    j = 0
    for i in reyting:
        user = data.get_user(i[0])
        if user:
            j += 1
            vaqt = f"{i[3] // 3600:02}:{i[3] % 3600 // 60:02}:{i[3] % 3600 % 60:02}"
            text += f"""

            <tr>
                <td>{j}</td>
                <td>{user.name}</td>
                <td>{user.phone}</td>
                <td>{i[2]}</td>
                <td>{vaqt}</td>
            </tr>
"""
    text += """

        </tbody>
    </table>
</body>
</html>
"""
    with open("stat.html", "w") as fayl:
        fayl.write(text)

    await message.answer_document(
        FSInputFile("stat.html"),
        caption="📊 Reyting"
    )      