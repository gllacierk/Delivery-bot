from aiogram import types

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
order_button = types.KeyboardButton("🚛Заказать доставку🚛")
cart_button = types.KeyboardButton("Корзина🛒")
help_button = types.KeyboardButton("Помощь❔")
test_button = types.KeyboardButton("TEST")

start_keyboard.add(order_button)
start_keyboard.add(cart_button, help_button)
