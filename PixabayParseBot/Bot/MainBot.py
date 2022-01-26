import logging

from aiogram import Bot, Dispatcher, executor, types

import KeyboardBot 

from aiogram.dispatcher.filters import Text

from MainParser import openSite

import asyncio

API_TOKEN = '5203228652:AAG8b5XMIDt7vsEVa8dr-55wTzyBDXNbYzE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#results
res=0
choice=''
resultsParsings = []
i = 0

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

	await message.answer(reply_markup = KeyboardBot.threeButtons, text = "Hello")
	await message.answer("It's bot for get data to site \"pixabay\". Choose category:\n   -Photos,\n   -Illustrations,\n   -Vectors,\n   -Videos,\n   -Music,\n   -Sound Effects.\nAll about Bot in /help.\n\nPlease choice from list subject for geting.", reply_markup=KeyboardBot.inline_kb)

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):

    await message.answer("It's bot help in get data to site \"Pixabay\". It's data you can use for self need. But know you use not a license goods. So it do bad. If to my go a message with a request about delete all data and my bot, then i necessarily all delete.\n\nThanks for read.")

@dp.callback_query_handler(Text(startswith='buttonAmount_'))
async def process_callback_button_amount(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса

	global res
	res = 0
	res = int(callback_query.data.split('_')[1])
	global i
	i += 0.5

	await bot.send_message(callback_query.from_user.id, f"You choice amount in {res} items.")
	# await bot.send_message("Please choice from list subject for geting.", reply_markup=KeyboardBot.inline_kb_2)
	await bot.answer_callback_query(callback_query.id)
	#await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_Start, text="Starting?")
	await bot.send_message(callback_query.from_user.id, "Programm starting. Please waiting and will tap /answer")

@dp.callback_query_handler(Text(equals='button1'))
async def process_callback_button1(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса

	global choice
	choice = ''
	choice = 'photos'
	global i
	i += 0.5

	await bot.send_message(callback_query.from_user.id, "You choice \"Photos\"")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_2, text="Please choice amount items for geting.")

@dp.callback_query_handler(Text(equals='button2'))
async def process_callback_button1(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса
	choice = 'button2'
	await bot.send_message(callback_query.from_user.id, "You choice \"Illustrations\"")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_2, text="Please choice amount items for geting.")

@dp.callback_query_handler(Text(equals='button3'))
async def process_callback_button1(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса
	choice = 'button3'
	await bot.send_message(callback_query.from_user.id, "You choice \"Vectors\"")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_2, text="Please choice amount items for geting.")

@dp.callback_query_handler(Text(equals='button4'))
async def process_callback_button1(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса
	choice = 'button4'
	await bot.send_message(callback_query.from_user.id, "You choice \"Videos\"")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_2, text="Please choice amount items for geting.")

@dp.callback_query_handler(Text(equals='button5'))
async def process_callback_button1(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса
	choice = 'button5'
	await bot.send_message(callback_query.from_user.id, "You choice \"Music\"")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_2, text="Please choice amount items for geting.")

@dp.callback_query_handler(Text(equals='button6'))
async def process_callback_button1(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса
	choice = 'button6'

	await bot.send_message(callback_query.from_user.id, "You choice \"Sound Effects\"")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, reply_markup=KeyboardBot.inline_kb_2, text="Please choice amount items for geting.")

#@dp.callback_query_handler(Text(equals='buttonStart'))
#async def process_callback_buttonStart(callback_query: types.CallbackQuery):
	# Тут нужно отпрвать метод парса
	#await bot.send_message(callback_query.from_user.id, "Programm starting. Please waiting and tapped /answer")
	#await bot.answer_callback_query(callback_query.id)

async def finish (wait_for):
	while True:
		global i
		if choice != '' and res != 0 and i == 1:
			resultsParsing_array = []
			url_array = []
			resultsParsings, urls = openSite(res, choice)		

			@dp.message_handler(commands=['answer'])
			async def send_finish(message: types.Message):

				for resultsParsing, url in zip (resultsParsings, urls):
					await bot.send_message (message.from_user.id, text = resultsParsing + '\n\n' + url)
					#await message.answer(url, disable_webpage_preview=True)
			i = 0
		await asyncio.sleep(wait_for)

if __name__ == '__main__':

	loop = asyncio.get_event_loop()
	loop.create_task(finish(5)) # поставим 10 секунд, в качестве теста
	executor.start_polling(dp, skip_updates=True)