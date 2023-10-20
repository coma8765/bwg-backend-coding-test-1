import asyncio
import logging

from src.adapters.messenger import get_messenger
from src.adapters.messenger.third_party.aiogram.config import AiogramConfig
from src.core.config import get_config
from src.domain.main import App

config = get_config()
logging.basicConfig(level=config.log_level)

messenger = get_messenger(AiogramConfig(config.telegram_api_token))

app = App(messenger, config.telegram_chat_id)


async def main():
    await messenger.startup()


if __name__ == "__main__":
    asyncio.run(main())
