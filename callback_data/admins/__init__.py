from aiogram import Router, F
from . import files
from . import vik

router = Router()

router.callback_query.register(files.del_file_answer, F.data.startswith("delfile"))
router.callback_query.register(vik.get_vik_answer, F.data.startswith("getvik"))
router.callback_query.register(vik.del_quiz_answer, F.data.startswith("delquiz"))
router.callback_query.register(vik.del_vik_answer, F.data.startswith("delvik"))
