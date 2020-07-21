from keyboards.default import start_keyboard
from loader import dp, cursor, connect
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


@dp.message_handler(Command("start"))               # Хендлер для команды старт
async def start_command(message: Message):
    hello_text = "Привет меня зовут Кира, я помогу вам заказать доставку из ресторана Milna, прямо к вашей двери ;)"
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    cursor.execute(f"""SELECT id FROM user_data WHERE id={user_id}""") # выбрать столбец id в таблице user_data, где id=user_id

    if cursor.fetchone() is None:               # если фунция не находит id пользователя в БД, создаем запись
        cursor.execute(f"""INSERT INTO user_data VALUES ({user_id},'{full_name}',NULL, NULL, NULL)""")
        connect.commit()
        await message.answer(text=hello_text, reply_markup=start_keyboard)
        print("New user registered")

    else:
        await message.answer(text="С возвращением!", reply_markup=start_keyboard)
        print("An old user has returned to us")


@dp.message_handler(Command("info"))                # Хендлер для команды хелп
async def start_menu(message: Message):
    hello_text = "Привет меня зовут Кира, я помогу вам заказать доставку из ресторана Milna, прямо к вашей двери ;)"
    await message.reply(text=hello_text, reply_markup=start_keyboard)
    print("start handler is executed")
