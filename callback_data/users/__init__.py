from aiogram import Router, F
from aiogram.filters import and_f
from . import vik
from . import stat
import states

router = Router()

router.callback_query.register(vik.start_vik_answer, F.data.startswith("usergetvik"))
router.callback_query.register(vik.next_test_answer, and_f(states.users.StatrtTest.quiz, F.data.startswith("nextquiz")))
router.callback_query.register(vik.end_test_next_test_answer, F.data.startswith("nextquiz"))
router.callback_query.register(stat.get_stat_vik, F.data.startswith("reytinggetvik"))
                               