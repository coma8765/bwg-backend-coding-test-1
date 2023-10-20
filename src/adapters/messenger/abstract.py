from abc import ABC, abstractmethod
from typing import Callable, Coroutine, Never

from src.adapters.messenger.models import (
    Message,
    MessageSource,
    PhotoMessageSource,
)


class Messenger(ABC):
    __slots__ = ()

    @abstractmethod
    async def send_photo(self, message: PhotoMessageSource):
        pass

    @abstractmethod
    async def send_message(self, message: MessageSource):
        pass

    @abstractmethod
    def set_message_handler(
        self, callback: Callable[[Message], Coroutine[None, None, Never]]
    ):
        pass

    async def startup(self):
        pass

    async def shutdown(self):
        pass
