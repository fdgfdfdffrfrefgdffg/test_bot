from aiogram.fsm.state import State, StatesGroup

class AddFileState(StatesGroup):
    file = State()

class AddVikState(StatesGroup):
    name = State()

class AddQuiz(StatesGroup):
    quiz = State()

class SentMessageState(StatesGroup):
    message = State()
