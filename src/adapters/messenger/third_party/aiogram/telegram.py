from logging import Logger
from typing import Callable, Coroutine, Never

from aiogram import Bot, Dispatcher, types

from src.adapters.messenger.abstract import Messenger
from src.adapters.messenger.models import (
    Message,
    MessageSource,
    PhotoMessageSource,
)
from src.adapters.messenger.third_party.aiogram.config import AiogramConfig
from src.adapters.messenger.third_party.aiogram.models import (
    TelegramMessage,
    from_telegram_message,
)
from src.core.logging import get_logger


class Aiogram(Messenger):
    __slots__ = ("_bot", "_dispatcher", "_logger", "_message_handler")

    _bot: Bot
    _dispatcher: Dispatcher
    _logger: Logger
    _message_handler: Callable[[Message], Coroutine[None, None, Never]]

    def __init__(self, config: AiogramConfig, *_, **__):
        self._logger = get_logger("third-party.aiogram")

        self._bot = Bot(config.api_token)
        self._dispatcher = Dispatcher()

        self._logger.debug("initialization is successful")

        self._dispatcher.message()(self._handle_message)

    async def _handle_message(self, message: types.Message):
        await self._message_handler(from_telegram_message(message))

    async def startup(self):
        user = await self._bot.get_me()

        self._logger.info(
            "startup is successful, current user id %s, name %s",
            user.id,
            user.username,
        )

        await self._dispatcher.start_polling(self._bot)

    async def send_message(self, message: MessageSource) -> Message:
        self._logger.debug("send message to %s", message.chat_id)

        result = await self._bot.send_message(
            message.chat_id,
            message.text,
        )

        return from_telegram_message(result)

    async def send_photo(self, message: PhotoMessageSource) -> TelegramMessage:
        self._logger.debug("send message with photo to %s", message.chat_id)

        result = await self._bot.send_photo(
            message.chat_id,
            message.photo.file_id,
            caption=message.text,
        )

        return from_telegram_message(result)

    def set_message_handler(
        self, callback: Callable[[Message], Coroutine[None, None, Never]]
    ):
        self._logger.debug("set message handler (%s)", str(callback))

        self._message_handler = callback
