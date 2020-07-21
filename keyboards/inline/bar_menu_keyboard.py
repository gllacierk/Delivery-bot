from aiogram import types

bar_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
pepsi_button = types.InlineKeyboardButton(text="Pepsi", callback_data="pepsi")
sprite_button = types.InlineKeyboardButton(text="Sprite", callback_data="sprite")
redbul_button = types.InlineKeyboardButton(text="RedBul", callback_data="redbul")
juice_button = types.InlineKeyboardButton(text="Сок", callback_data="juice")
william_button = types.InlineKeyboardButton(text="William Lawson`s", callback_data="william")
henessy_button = types.InlineKeyboardButton(text="Hennessy", callback_data="hennessy")
back_button = types.InlineKeyboardButton(text="В главное меню", callback_data="back")

bar_menu_keyboard.add(pepsi_button, sprite_button, redbul_button, juice_button,
                      william_button, henessy_button, back_button)
