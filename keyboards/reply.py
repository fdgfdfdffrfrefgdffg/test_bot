from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButtonPollType

user_menu = ReplyKeyboardBuilder()
user_menu.button(text="❔ Test yechish")
user_menu.button(text="📂 Foydali fayllar")
user_menu.button(text="📊 Reyting")
user_menu = user_menu.as_markup()
user_menu.resize_keyboard = True
user_menu.is_persistent = True

phone_menu = ReplyKeyboardBuilder()
phone_menu.button(text="Telefon raqamni yuborish uchun bosing", request_contact=True)
phone_menu = phone_menu.as_markup()
phone_menu.resize_keyboard = True
phone_menu.is_persistent = True

admin_menu = ReplyKeyboardBuilder()
admin_menu.button(text="📂 Fayllar")
admin_menu.button(text="❔ Testlar")
admin_menu.button(text="✍️ Xabar yuborish")
admin_menu = admin_menu.as_markup()
admin_menu.resize_keyboard = True
admin_menu.is_persistent = True

cancel_menu = ReplyKeyboardBuilder()
cancel_menu.button(text="🚫 Bekor qilish")
cancel_menu = cancel_menu.as_markup()
cancel_menu.resize_keyboard = True
cancel_menu.is_persistent = True

files_menu = ReplyKeyboardBuilder()
files_menu.button(text="➕ Fayl qo'shish")
files_menu.button(text="🚫 Bekor qilish")
files_menu = files_menu.as_markup()
files_menu.resize_keyboard = True
files_menu.is_persistent = True


viks_menu_admin = ReplyKeyboardBuilder()
viks_menu_admin.button(text="➕ Viktorina qo'shish")
viks_menu_admin.button(text="🚫 Bekor qilish")
viks_menu_admin = viks_menu_admin.as_markup()
viks_menu_admin.resize_keyboard = True
viks_menu_admin.is_persistent = True

vik_menu_admin = ReplyKeyboardBuilder()
vik_menu_admin.button(text="➕ Test qo'shish")
vik_menu_admin.button(text="📊 Reyting")
vik_menu_admin.button(text="🚫 Bekor qilish")
vik_menu_admin = vik_menu_admin.as_markup()
vik_menu_admin.resize_keyboard = True
vik_menu_admin.is_persistent = True

add_quiz_menu = ReplyKeyboardBuilder()
add_quiz_menu.button(text="Test yaratish", request_poll=KeyboardButtonPollType(type="quiz"))
add_quiz_menu.button(text="🚫 Bekor qilish")
add_quiz_menu = add_quiz_menu.as_markup()
add_quiz_menu.resize_keyboard = True
add_quiz_menu.is_persistent = True

check_join_btn = ReplyKeyboardBuilder()
check_join_btn.button(text="✅ Tekshirish")
check_join_btn = check_join_btn.as_markup()
check_join_btn.resize_keyboard = True
check_join_btn.is_persistent = True