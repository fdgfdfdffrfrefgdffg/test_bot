from aiogram import Router
from . import admins
from . import users

router = Router()

router.include_router(admins.router)
router.include_router(users.router)
