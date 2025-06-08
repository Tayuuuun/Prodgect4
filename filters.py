from aiogram import types
from aiogram.filters import Filter

class IsCityFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        if not message.text:
            return False

        text = message.text.strip()
        words = text.split()

        if len(words) != 1:
            return False

        city = words[0]

        if not city.isalpha():
            return False

        return True
