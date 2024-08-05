from aiogram import Router, F
from . import start
from . import notsub
from . import files
from . import canccel
from . import stat
from . import vik
import states
import filters

router = Router()

router.message.register(notsub.not_sub_channel_answer, filters.IsNotSubChannel())
router.message.register(start.answer_name, states.users.RegisterState.name)
router.message.register(start.answer_phone, states.users.RegisterState.phone)
router.message.register(start.start_not_user, filters.IsNotDB())
router.message.register(notsub.check_join_answer, F.text == "✅ Tekshirish")
router.message.register(canccel.cancel_answer, F.text == "🚫 Bekor qilish")
router.message.register(start.start_db_user, F.text == "/start")
router.message.register(files.get_files, F.text == "📂 Foydali fayllar")
router.message.register(vik.get_viks_answer, F.text == "❔ Test yechish")
router.message.register(stat.get_stat_vik, F.text == "📊 Reyting")
router.message.register(notsub.not_understand)
router.poll_answer.register(vik.get_quiz_answer, states.users.StatrtTest.quiz)
