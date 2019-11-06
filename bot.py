# импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# добавляем логирование для нашего бота
import logging

# импортируем настройки из файла settings в котором наш api и proxy
import settings

# комманда для логирования
logging.basicConfig(format="%(asctime)s- %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="bot.log"
                    )

# создаем функцию, которая вызывается при нажатии кнопки старт
def greet_user (bot,update):
    text = "нажали старт /start"
    logging.info(text)
    print(text)
    update.message.reply_text(text)

# функция которая будет отвечать пользователю
def talk_to_me (bot,update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name,update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                    update.message.chat.id, update.message.text)
    print(update.message)
    update.message.reply_text(user_text)

# функция которая соединяется с платформой телеграм , тело бота
def main():
    mybot = Updater (settings.API_KEY , request_kwargs=settings.PROXY)

    logging.info("Бот запускается")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


# вызываем функция, строчка запускает нашего бота

main()
