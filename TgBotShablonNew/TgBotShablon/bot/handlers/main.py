from aiogram import html, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

from db.models import User

main_router = Router()
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = await User.get(id_ = message.from_user.id)
    if not user:
        await User.create(id = message.from_user.id , fullname = message.from_user.full_name)
    await message.answer(_("Hello, {}!").format({html.bold(message.from_user.full_name)}))

