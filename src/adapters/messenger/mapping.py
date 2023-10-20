from src.adapters.messenger.abstract import Messenger
from src.adapters.messenger.third_party.aiogram.telegram import Aiogram


def get_messenger(*args, **kwargs) -> Messenger:
    return Aiogram(*args, **kwargs)
