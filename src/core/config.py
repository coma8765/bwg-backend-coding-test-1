"""Application environment configuration provider

Copy `.env.example` to `.env` for pure usa
or to `.env.docker` for docker-based use.
Or setup environment variables use system methods.
"""
import logging
from dataclasses import dataclass
from functools import lru_cache

from environs import Env


@dataclass
class Config:
    log_level: int
    telegram_api_token: str
    telegram_chat_id: int


@lru_cache()
def get_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        log_level=env.log_level("LOG_LEVEL", logging.INFO),
        telegram_api_token=env.str("TELEGRAM_API_TOKEN"),
        telegram_chat_id=env.int("TELEGRAM_CHAT_ID"),
    )


__all__ = ["get_config", "Config"]
