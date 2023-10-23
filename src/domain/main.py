"""Main use-case implementation"""
import json
from logging import Logger

from src.adapters.messenger import (
    Message,
    MessageSource,
    Messenger,
    PhotoMessageSource,
)
from src.core.logging import get_logger


class App:
    """The main use-case of the application

    This use-case using `locales.json` for multi-language support.
    """

    __slots__ = ("_logger", "_messenger", "locales", "_chat_id")

    _logger: Logger
    _messenger: Messenger
    _chat_id: int
    locales: dict[str, dict[str, str]]

    def __init__(self, messanger: Messenger, chat_id: int):
        self._logger = get_logger("main")
        self._messenger = messanger
        self._chat_id = chat_id

        self.load_locales()

        messanger.set_message_handler(callback=self._message_handler)

    def load_locales(self):
        self._logger.debug("load locales")
        with open("src/assets/translates.json", "r", encoding="utf-8") as f:
            self.locales = json.load(f)

    async def _message_handler(self, message: Message):
        if message.chat_id == self._chat_id:
            return

        if message.language_code not in self.locales.keys():
            locale = self.locales["ru"]
        else:
            locale = self.locales[message.language_code]

        if message.text == "/start":
            text = f"{locale['start']} {locale['task']}"

            await self._messenger.send_message(
                MessageSource(message.chat_id, text)
            )
            return

        fail_message = None
        if not message.photos:
            fail_message = locale["fail-photo"]
        elif not message.text or len(message.text.split()) not in (2, 3):
            fail_message = locale["fail-full-name"]

        if fail_message or not message.photos:
            text = f"{locale['task']} {fail_message or ''}"

            await self._messenger.send_message(
                MessageSource(message.chat_id, text)
            )
        else:
            self._logger.debug("got new screen + full name")
            await self._messenger.send_message(
                MessageSource(
                    message.chat_id,
                    locale["success"],
                )
            )

            await self._messenger.send_photo(
                PhotoMessageSource(
                    self._chat_id,
                    str(message.text),
                    photo=message.photos[0],
                )
            )


__all__ = ["App"]
