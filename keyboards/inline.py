from aiogram.utils.keyboard import InlineKeyboardBuilder

def channels_btn(channels):
    markup = InlineKeyboardBuilder()
    for index, channel in enumerate(channels, start=1):
        markup.button(text=f"{index}-kanal", url=channel['url'])
    markup.adjust(1)
    return markup.as_markup()

def del_fayl_btn(file_id):
    markup = InlineKeyboardBuilder()
    markup.button(text="❌ Faylni o'chirish", callback_data=f"delfile:{file_id}")
    return markup.as_markup()

def get_viks_btn(viks, admin=None):
    markup = InlineKeyboardBuilder()
    for i in viks:
        if admin:
            markup.button(text=i[1], callback_data=f"getvik:{i[0]}")
            markup.button(text="❌", callback_data=f"delvik:{i[0]}")
        else:
            markup.button(text=i[1], callback_data=f"usergetvik:{i[0]}")

    markup.adjust(2)
    return markup.as_markup()

def get_viks_for_reyting_btn(viks):
    markup = InlineKeyboardBuilder()
    for i in viks:
        markup.button(text=i[1], callback_data=f"getvikreyting:{i[0]}")
    markup.adjust(2)
    return markup.as_markup()

def del_quiz_btn(quiz_id):
    markup = InlineKeyboardBuilder()
    markup.button(text="❌ Testni o'chirish", callback_data=f"delquiz:{quiz_id}")
    return markup.as_markup()

next_test_btn = InlineKeyboardBuilder()
next_test_btn.button(text="Keyingi savol", callback_data="nextquiz")
next_test_btn = next_test_btn.as_markup()
