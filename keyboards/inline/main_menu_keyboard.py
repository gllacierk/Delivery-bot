from aiogram import types

make_order_keyboard = types.InlineKeyboardMarkup(row_width=2)
pizza_button = types.InlineKeyboardButton("Пицца", callback_data="pizza_menu")
sushi_button = types.InlineKeyboardButton("Суши и роллы", callback_data="sushi_menu")
bar_button = types.InlineKeyboardButton("Барная карта", callback_data="bar_menu")
hookah_button = types.InlineKeyboardButton("Кальянное меню", callback_data="hookah_menu")

make_order_keyboard.add(pizza_button, sushi_button, bar_button, hookah_button)
