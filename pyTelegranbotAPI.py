import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените на свой токен бота
TOKEN = 'YOUR_BOT_TOKEN'

# Замените на @username или ID вашего канала
CHANNEL_ID = '@your_channel_username'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Используй /check для проверки подписки на канал.')


def check_subscription(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    chat_member = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        update.message.reply_text(f"Вы подписаны на канал {CHANNEL_ID}!")
    else:
        update.message.reply_text(f"Вы не подписаны на канал {CHANNEL_ID}. Пожалуйста, подпишитесь!")


def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check", check_subscription))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()