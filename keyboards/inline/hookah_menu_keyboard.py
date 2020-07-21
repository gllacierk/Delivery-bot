from aiogram import types

hookah_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
dark_button = types.InlineKeyboardButton(text="DarkSide", callback_data="dark_side")
nakhla_button = types.InlineKeyboardButton(text="Nakhla", callback_data="nakhla")
satyr_button = types.InlineKeyboardButton(text="Satyr", callback_data="satyr")
serbet_button = types.InlineKeyboardButton(text="Serbetli", callback_data="serbetli")
back_button = types.InlineKeyboardButton(text="В главное меню", callback_data="back")

hookah_menu_keyboard.add(dark_button, nakhla_button, satyr_button,
                         serbet_button, back_button)
