from aiogram import types

pizza_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
pepperoni_button = types.InlineKeyboardButton(text="Пепперони", callback_data="pizza_001")
four_seasons_button = types.InlineKeyboardButton(text="Четыре сезона", callback_data="pizza_002")
brand_name_button = types.InlineKeyboardButton(text="Фирменная", callback_data="pizza_003")
mushroom_button = types.InlineKeyboardButton(text="Грибная", callback_data="pizza_004")
back_button = types.InlineKeyboardButton(text="В главное меню", callback_data="back")

pizza_menu_keyboard.add(pepperoni_button, four_seasons_button, brand_name_button,
                        mushroom_button, back_button)
