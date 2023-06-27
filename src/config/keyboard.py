from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


command_task = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton("/list"))
    .add(KeyboardButton("/add"))
    .add(KeyboardButton("/done"))
    .add(KeyboardButton("/delete"))
)


remove_keyboard = ReplyKeyboardRemove()
