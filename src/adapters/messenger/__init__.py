"""The Messenger provider

Usage:
    messanger = get_messenger(config=...)
    messanger.set_message_handler(message_callback)

    messanger.send_message(
        MessageSource(
            chat_id=-1,
            text="message text",
        )
    )
"""
from src.adapters.messenger.abstract import *
from src.adapters.messenger.mapping import *
from src.adapters.messenger.models import *
