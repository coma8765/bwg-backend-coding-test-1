"""Enables use of Application as a "main" function (i.e. "python -m src").

This module prepares third party libraries
and provides them to the domain application.
"""
import asyncio

from src.adapters.messenger import get_messenger
from src.adapters.messenger.third_party.aiogram import AiogramConfig
from src.core import Config, configure_logging, get_config, get_logger
from src.domain import App


async def main(config: Config):  # Async application bootstrap
    logger = get_logger()
    logger.info("initialize the application")
    messenger = get_messenger(AiogramConfig(config.telegram_api_token))

    logger.info("startup the application")

    App(messenger, config.telegram_chat_id)  # Init main application

    await messenger.startup()


if __name__ == "__main__":
    env_config = get_config()
    configure_logging(level=env_config.log_level)

    asyncio.run(main(env_config))

__all__: list[str] = []
