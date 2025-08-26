# bot.py
import os
print("Запуск бота...")
TOKEN = os.getenv("BOT_TOKEN")
if TOKEN:
    print("Токен загружен")
else:
    print("ТОКЕН НЕ НАЙДЕН!")
