from aiogram import Bot,Dispatcher,executor

import config

bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(dp):
    print("I started")

if __name__ == "__main__":
    executor.start_polling(dp,on_startup=on_startup)