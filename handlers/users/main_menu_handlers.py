from loader import dp, bot
from data import config
from keyboards.inline import make_order_keyboard
from aiogram.types import Message


@dp.message_handler(text="🚛Заказать доставку🚛")       # Хендлер для кнопки Заказать доставку
async def make_order(message: Message):
    photo = open("media/menu.png", "rb")
    menu_text = "Основной раздел меню, выбирайте!"
    await message.answer_photo(photo=photo, caption=menu_text, reply_markup=make_order_keyboard)
    print("make order handler is executed")


@dp.message_handler(text="Помощь❔")                  # Хендлер для команды Помощь
async def help_user(message: Message):
    photo = open("media/noproblem.jpg", "rb")
    problem_text = 'Напишите нам как показано на скриншоте\nМы вам объязательно поможем!'
    await message.answer_photo(photo=photo, caption=problem_text, disable_notification=True)
    photo.close()
    print("help handler is executed")


@dp.message_handler(regexp="Проблема:")             # Хендлер для пересылки сообщения о проблеме админу
async def send_problem_admin(message: Message):

    await bot.send_message(chat_id=config.admin_id,
                           text=f"Пользователь: {message.from_user.full_name}\nid: {message.from_user.id}\n"
                                    f"Написал о проблеме: {message.text}")
    print("problem message send to admin")


@dp.message_handler(text="Корзина🛒")                 # Хендлер для корзины
async def open_cart(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text="Раздел в разработке 😁")
    print("Open cart handler is executed")
