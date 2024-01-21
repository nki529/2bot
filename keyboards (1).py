from telebot import types
btn1 = types.KeyboardButton("/start")
btn2 = types.KeyboardButton("/item")
btn3 = types.KeyboardButton("/hero")
btn4 = types.KeyboardButton("/hello")
menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2,btn3,btn4)




Inmenu = types.InlineKeyboardMarkup(row_width=12)
Inmune = types.InlineKeyboardMarkup(row_width=2)
inlbn1 = types.InlineKeyboardButton(text = "1",callback_data="1")
inlbn2 = types.InlineKeyboardButton(text = "2",callback_data="2")
inlbn3 = types.InlineKeyboardButton(text = "3",callback_data="3")
inlbn4 = types.InlineKeyboardButton(text = "4",callback_data="4")
inlbn5 = types.InlineKeyboardButton(text = "5",callback_data="5")
inlbn6 = types.InlineKeyboardButton(text = "6",callback_data="6")
inlbn7 = types.InlineKeyboardButton(text = "7",callback_data="7")
inlbn8 = types.InlineKeyboardButton(text = "8",callback_data="8")
inlbn9 = types.InlineKeyboardButton(text = "9",callback_data="9")
Inmune.add(inlbn1,inlbn2,inlbn3,inlbn4,inlbn5,inlbn6,inlbn7,inlbn9,inlbn8)
#InMenu = types.InlineKeyboardMarkup(pow_width=2)
#inBtn = 