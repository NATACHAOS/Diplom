import telebot
from time import sleep
import asyncio

"""Создан телеграм-бот https://t.me/NATACHAOS_hi_bot.
При отправке в чате "/start" в ответ придёт "Привет". При отправке в чате "/stop" - программа завершается.
Как только программа завершается, на консоль выводится "Кто-то захотел здрасти" """


async def notification1():
    sleep(1)
    print("Кто-то захотел здрасти")


async def main1():
    task = asyncio.create_task(notification1())  # Программа завершается и выводится "Кто-то захотел здрасти"
    API_TOKEN = '7217572375:AAHSzdTy_v6kFVzZFbS7Jxvzes0Esap059Q'
    bot = telebot.TeleBot(API_TOKEN)

    # При написании /start в боте в ответ придёт "Привет"
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, "Привет")

    # При написании /stop в боте - программа завершится
    @bot.message_handler(commands=['stop'])
    def stop(message):
        bot.stop_polling()

    bot.polling()


asyncio.run(main1())
