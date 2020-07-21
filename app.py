from loader import bot, storage, connect, cursor
from data import config
from keyboards.default import start_keyboard


async def on_startup(dp):
    await bot.send_message(chat_id=config.admin_id, text="Bot is up", reply_markup=start_keyboard)


async def on_shutdown(dp):
    await bot.close()
    await storage.close()
    await connect.close()
    await cursor.close()

if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
