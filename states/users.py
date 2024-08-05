from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    name = State()
    phone = State()

class SubChannelState(StatesGroup):
    sub = State()

class StatrtTest(StatesGroup):
    quiz = State()