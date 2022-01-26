from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Keybaoard

startButton = KeyboardButton('/start')
answerButton = KeyboardButton('/answer')
helpButton = KeyboardButton('/help')

threeButtons = ReplyKeyboardMarkup(resize_keyboard = True)

threeButtons.row(startButton, answerButton).add(helpButton)



button1 = InlineKeyboardButton('Photos', callback_data='button1')
#button2 = InlineKeyboardButton('Illustrations', callback_data='button2')
#button3 = InlineKeyboardButton('Vectors', callback_data='button3')
#button4 = InlineKeyboardButton('Videos', callback_data='button4')
#button5 = InlineKeyboardButton('Music', callback_data='button5')
#button6 = InlineKeyboardButton('Sound Effects', callback_data='button6')

#inline_kb = InlineKeyboardMarkup().row(button1, button2).row(button3, button4).row(button5, button6)

inline_kb = InlineKeyboardMarkup().add(button1)

button_amount_1 = InlineKeyboardButton('1', callback_data='buttonAmount_1')
button_amount_10 = InlineKeyboardButton('10', callback_data='buttonAmount_10')
button_amount_50 = InlineKeyboardButton('20', callback_data='buttonAmount_20')
button_amount_100 = InlineKeyboardButton('30', callback_data='buttonAmount_30')
button_amount_200 = InlineKeyboardButton('40', callback_data='buttonAmount_40')
button_amount_300 = InlineKeyboardButton('50', callback_data='buttonAmount_50')
button_amount_400 = InlineKeyboardButton('60', callback_data='buttonAmount_60')
button_amount_500 = InlineKeyboardButton('100', callback_data='buttonAmount_100')
#button_amount_600 = InlineKeyboardButton('Photos', callback_data='button_amount_600')
#button_amount_700 = InlineKeyboardButton('Photos', callback_data='button_amount_700')
#button_amount_800 = InlineKeyboardButton('Photos', callback_data='button_amount_800')
#button_amount_900 = InlineKeyboardButton('Photos', callback_data='button_amount_900')
#button_amount_1000 = InlineKeyboardButton('Photos', callback_data='button_amount_1000')

inline_kb_2 = InlineKeyboardMarkup().row(button_amount_1, button_amount_200).row(button_amount_10, button_amount_300).add(button_amount_50, button_amount_400).add(button_amount_100, button_amount_500)

#buttonStart = InlineKeyboardButton('Start', callback_data='buttonStart')

#inline_kb_Start = InlineKeyboardMarkup().add(buttonStart)