"""Tests for Telegram adapter"""
from datetime import datetime
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch

from aiogram import Bot, types

from src.adapters.messenger.models import MessageSource
from src.adapters.messenger.third_party.aiogram import Aiogram, AiogramConfig


class TestAiogram(IsolatedAsyncioTestCase):
    """Test cases for aiogram Telegram adapter"""

    instance: Aiogram

    @classmethod
    def setUpClass(cls):
        cls.instance = Aiogram(AiogramConfig(api_token="1:test"))

    def test_config(self):
        test_config = AiogramConfig(api_token="2:test-case")
        instance = Aiogram(test_config)
        bot: Bot = getattr(instance, "_bot")

        self.assertEqual(
            test_config.api_token, bot.token, msg="configuration fail"
        )

    async def test_send_message(self):
        test_message_source = MessageSource(1, "test-text-1")
        test_message = MessageSource(2, "test-text-2")

        response_message = types.Message(
            message_id=0,
            chat=types.Chat(id=test_message.chat_id, type="chat", title=""),
            text=test_message.text,
            date=datetime.now(),
        )

        send_message = AsyncMock(return_value=response_message)

        with patch.object(
            Bot,
            "send_message",
            side_effect=send_message,
        ):
            message = await self.instance.send_message(test_message_source)

        self.assertEqual(message.chat_id, test_message.chat_id)
        self.assertEqual(message.text, test_message.text)
        send_message.assert_called_once_with(
            test_message_source.chat_id,
            test_message_source.text,
        )

    # TODO: @coma8765 Add other tests
