from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatMemberStatus
from consts import CHANNELS
import keyboards.reply
import states
import keyboards
import data

async def not_sub_channel_answer(message: Message, bot: Bot, state: FSMContext):
    not_sub_channels = []
    for channel in CHANNELS:
        status = await bot.get_chat_member(channel['id'], message.from_user.id)
        status = status.status
        if not (status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER)):
            not_sub_channels.append(channel)
    
    await message.answer("Quydagi kanallarga obuna bo'ling!", reply_markup=keyboards.inline.channels_btn(not_sub_channels))
    
async def not_understand(message: Message):
    pass