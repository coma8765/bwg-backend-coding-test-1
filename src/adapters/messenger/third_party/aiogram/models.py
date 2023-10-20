from dataclasses import dataclass

from aiogram.types.message import Message as _TelegramMessage

from src.adapters.messenger.models import Message, Photo


@dataclass(kw_only=True)
class TelegramMessage(Message):
    _original: _TelegramMessage


def from_telegram_message(
    origin: _TelegramMessage,
) -> TelegramMessage:
    photos: list[Photo] | None = None

    if origin.photo is not None:
        photos = [Photo(photo.file_id) for photo in origin.photo]

    language_code = getattr(
        origin.from_user, "language_code", Message.language_code
    )

    return TelegramMessage(
        chat_id=origin.chat.id,
        text=origin.text or origin.caption,
        photos=photos,
        language_code=language_code,
        _original=origin,
    )
