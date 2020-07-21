from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline import pizza_menu_keyboard, sushi_menu_keyboard, bar_menu_keyboard, hookah_menu_keyboard


@dp.callback_query_handler(text="pizza_menu")               # Хендлер для кнопки Пицца
async def sushi_menu(call: CallbackQuery):
    photo = open("media/pizza.jpg", "rb")

    await call.answer(cache_time=60)
    await call.message.answer_photo(photo=photo, caption="🍕 Сегодня в меню 🍕",
                                    reply_markup=pizza_menu_keyboard)
    photo.close()
    print("Pizza handler is executed")


@dp.callback_query_handler(text="sushi_menu")               # Хендлер для кнопки Суши и роллы
async def sushi_menu(call: CallbackQuery):
    photo = open("media/sushi.jpg", "rb")

    await call.answer(cache_time=60 )
    await call.message.answer_photo(photo=photo, caption="🍣 Cегодня в меню 🍣",
                                    reply_markup=sushi_menu_keyboard)
    photo.close()
    print("Sushi handler is executed")


@dp.callback_query_handler(text="bar_menu")                 # Хендлер для кнопки Барная карта
async def bar_menu(call: CallbackQuery):
    photo = open("media/bar.jpg", "rb")

    await call.answer(cache_time=60)
    await call.message.answer_photo(photo=photo,caption="Сегодня в баре 🍷🍺🥃",
                                    reply_markup=bar_menu_keyboard)
    photo.close()
    print("Bar handler is executed")


@dp.callback_query_handler(text="hookah_menu")              # Хендлер для кнопки Кальянное меню
async def bar_menu(call: CallbackQuery):
    photo = open("media/hookah.jpg", "rb")

    await call.answer(cache_time=60)
    await call.message.answer_photo(photo=photo, caption="Давай подымим? 😉💨",
                                    reply_markup=hookah_menu_keyboard)
    photo.close()
    print("Hookah menu handler is executed")
