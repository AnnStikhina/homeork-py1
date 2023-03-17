from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message


bot_gb = Bot("6145199891:AAFhCdmMKFUjBASbUEmk38R5vcrhsq3JqrQ")
dp = Dispatcher(bot_gb)

async def on_start(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    await message.reply('Бот запущен и готов к работе')


@dp.message_handler()
async def com_start(message: Message):
    if message.text == 'пойдем гулять':
        await message.answer(f'Погнали, {message.from_user.first_name},' f' прогуляемся')
    elif message.text == 'выпьем кофе':
        await message.answer(f'я буду Латте')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)