from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline import make_order_keyboard


@dp.callback_query_handler(text="back")
async def pizza_back(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = open("media/menu.png", "rb")
    menu_text = "Основной раздел меню, выбирайте!"
    await call.message.answer_photo(photo=photo, caption=menu_text, reply_markup=make_order_keyboard)
    photo.close()
    print("Back handler is executed")