from aiogram import types

sushi_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
philadelphia_button = types.InlineKeyboardButton(text='Сет "Филадельфия"', callback_data="sushi_001")
admiral_set_button = types.InlineKeyboardButton(text='Сет "Адмирал"', callback_data="sushi_002")
patriot_set = types.InlineKeyboardButton(text='Сет "Патриот"', callback_data="sushi_003")
party_set_button = types.InlineKeyboardButton(text='Сет "Пати на хате"', callback_data="sushi_004")
back_button = types.InlineKeyboardButton(text="В главное меню", callback_data="back")


sushi_menu_keyboard.add(philadelphia_button, admiral_set_button, patriot_set,
                        party_set_button, back_button)
