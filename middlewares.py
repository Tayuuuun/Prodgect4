from aiogram import types
import logging

class LoggingMiddleware:
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"User {message.from_user.id}: {message.text}")
