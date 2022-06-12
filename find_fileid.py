
import config 
import logging 
from aiogram import *
#'490557903' 
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)
a = []
@dp.message_handler(content_types=types.ContentType.all())
async def get_message(message: types.Message):
    if message.content_type == 'animation' and message.from_user.id == 490557903:
        a.append(message.animation.file_id)
        print(a)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)