from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio
import keyboards

bot = Bot(token="6798745111:AAH_CBOpDiLuKxIxeMbnaSr-DzRzoqzFbr0")
dp = Dispatcher()


@dp.message(F.text == '/start')
async def start(message):
    await bot.delete_message(message.chat.id, message.message_id)
    # await bot.delete_message(message.chat.id, message.message_id-1)
    await bot.send_message(message.chat.id, "Menu:", reply_markup=keyboards.menu_kb)


@dp.message(F.text == '🎥 Choose film')
async def chose_film(message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id-1)
    await bot.send_message(message.chat.id, "How do you want to choose a film:", reply_markup=keyboards.chose_film_kb)


@dp.message(F.text == '⬅️ Back')
async def back(message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id-1)
    await bot.send_message(message.chat.id, "Menu:", reply_markup=keyboards.menu_kb)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
