from aiogram import Router, F
from aiogram.filters import and_f
import filters
from . import start
from . import files
from . import vik
from . import cancel
from . import sent
from . import stat
import states

router = Router()

router.message.register(cancel.cancel_answer, and_f(filters.IsAdmin(), F.text == "🚫 Bekor qilish"))
router.message.register(files.add_file_file_answer, states.admins.AddFileState.file)
router.message.register(vik.add_vik_name_answer, states.admins.AddVikState.name)
router.message.register(sent.answer_sent_message, states.admins.SentMessageState.message)
router.message.register(vik.add_quiz_answer, states.admins.AddQuiz.quiz)
router.message.register(start.start, and_f(filters.IsAdmin(),  F.text == "/start"))
router.message.register(vik.get_viks, F.text == "❔ Testlar")
router.message.register(vik.add_vik_answer, F.text == "➕ Viktorina qo'shish")
router.message.register(sent.answer_sent, and_f(filters.IsAdmin(),  F.text == "✍️ Xabar yuborish"))
router.message.register(files.choose_category_answer, and_f(filters.IsAdmin(),  F.text == "📂 Fayllar"))
router.message.register(files.get_files, and_f(filters.IsAdmin(), filters.GetFilesFilter()))
router.message.register(files.add_file_answer, and_f(filters.IsAdmin(),  F.text == "➕ Fayl qo'shish"))
router.message.register(vik.add_vik_quiz_answer, and_f(filters.IsAdmin(),  F.text == "➕ Test qo'shish"))
router.message.register(stat.get_stat_vik, and_f(filters.IsAdmin(),  F.text == "📊 Reyting"))
router.message.register(cancel.empty, filters.IsAdmin() )

