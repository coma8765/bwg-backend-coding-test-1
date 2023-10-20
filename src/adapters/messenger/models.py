from dataclasses import dataclass


@dataclass
class Photo:
    """The entity for the photo"""

    file_id: str


@dataclass
class MessageSource:
    """The entity of the message to send"""

    chat_id: int
    text: str


@dataclass
class PhotoMessageSource(MessageSource):
    """The entity of the message to send"""

    photo: Photo


@dataclass
class Message:
    """The entity of the already sent message"""

    chat_id: int
    text: str | None = None
    photos: list[Photo] | None = None
    language_code: str = "ru"
