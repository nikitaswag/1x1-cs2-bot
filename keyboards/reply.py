from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Профиль 👤")],
    [KeyboardButton(text= "Пригласить соперника⚔️")],
    [KeyboardButton(text= "Кейсы 🎰"), KeyboardButton(text= "Поддержка 🚔")],
    [KeyboardButton(text= "Вывод средств 💰"),
    KeyboardButton(text= "Пополнить баланс 💸")],
],
resize_keyboard=True
)