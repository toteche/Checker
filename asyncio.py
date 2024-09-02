import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command

# Замените на свой токен бота
API_TOKEN = 'YOUR_BOT_TOKEN'

# Замените на @username или ID вашего канала
CHANNEL_ID = '@your_channel_username'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привет! Используй /check для проверки подписки на канал.")


@dp.message_handler(Command("check"))
async def cmd_check(message: types.Message):
    user_id = message.from_user.id

    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            await message.reply(f"Вы подписаны на канал {CHANNEL_ID}!")
        else:
            await message.reply(f"Вы не подписаны на канал {CHANNEL_ID}. Пожалуйста, подпишитесь!")
    except Exception as e:
        await message.reply("Произошла ошибка при проверке подписки. Пожалуйста, попробуйте позже.")
        print(f"Error checking subscription: {e}")


async def main():
    # Запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())