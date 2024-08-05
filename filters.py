from consts import CHANNELS, ADMIN
from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import Filter
from aiogram.enums import ChatMemberStatus
import data

class IsNotSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        not_sub_channels = []
        for channel in CHANNELS:
            status = await bot.get_chat_member(channel['id'], message.from_user.id)
            status = status.status
            if not (status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER)):
                not_sub_channels.append(channel)
        
        return bool(not_sub_channels)

class IsNotDB(Filter):
    async def __call__(self, message: Message):
        return not bool(data.get_user(message.from_user.id))

class IsAdmin(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id == ADMIN