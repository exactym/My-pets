import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers import router

async def main():
    load_dotenv()
    bot = Bot(token = os.getenv('TG_TOKEN'))
    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(router)
    await dp.start_polling(bot) 

async def startup(dispatcher: Dispatcher):
    print('запуск бота...')
async def shutdown(dispatcher: Dispatcher):
    print('остановка работы бота...')
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('Выход')
        
    
    
           

