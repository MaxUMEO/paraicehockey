from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext


def about_federation_keyboard():
    keyboard = [
        [InlineKeyboardButton('Ценности Федерации',
                              callback_data='fed_values')],
        [InlineKeyboardButton('Направления деятельности',
                              callback_data='fed_activities')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)


def go_back_keyboard_for_values():
    keyboard = [
        [InlineKeyboardButton('Направления деятельности',
                              callback_data='fed_activities')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)


def go_back_keyboard_for_activities():
    keyboard = [
        [InlineKeyboardButton('Ценности Федерации',
                              callback_data='fed_values')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)


def about_fed_main_page(update: Update, context: CallbackContext):
    """Функция для первого сообщения о Федерации, с меню."""
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/about_fed_1.png', 'rb'))
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/about_fed_2.png', 'rb'),
                           reply_markup=about_federation_keyboard())


def fed_values_page(update: Update, context: CallbackContext):
    """Функция для отображения 'ценности Федерации'."""
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/values.png', 'rb'),
                           reply_markup=go_back_keyboard_for_values())


def fed_activities_page(update: Update, context: CallbackContext):
    """Функция для отображения 'Направления деятельности'."""
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/fed_activities.png', 'rb'),
                           reply_markup=go_back_keyboard_for_activities())
