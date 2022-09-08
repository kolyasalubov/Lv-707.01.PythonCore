import telebot
from TOKEN import TELEGRAM_TOKEN
import calculate

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        f"Привіт, {message.chat.first_name}{message.chat.last_name or ''}!\n"
    )   
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton("Мариновані\n" 
                                            "помідори \U0001F345")
    itembtn2 = telebot.types.KeyboardButton("Мариновані\n"
                                            "огірки \U0001F952")
    markup.row(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Виберіть рецепт із меню \U0001F447", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_tomato_cucumber_recipe(message):
    if message.text == ("Мариновані\n"
                        "помідори \U0001F345"):
        bot.send_message(
        message.chat.id,
        "<b>Інгредієнти:\n</b>"
        "помідори\n"
        "кріп із парасольками\n"
        "часник\n"
        "чорний перець горошок\n"
        "листя смородини\n"
        "листя вишні\n\n"
        "<b>Маринад на 1.5 літра води:</b>\n"
        "вода - 1.5 л.\n"
        "цукор - 6 ст.л.\n"
        "оцет - 85 мл.\n"
        "сіль - 1.5 ст.л.",
        parse_mode="HTML"
    )

        tomato_photo = open("bot_project\IMG_6237.png", "rb")
        bot.send_photo(message.chat.id, tomato_photo)
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn = telebot.types.KeyboardButton("Розрахунок маринаду для помідорів")
        itembtn_back = telebot.types.KeyboardButton("Назад до меню \U000021A9")
        markup.row(itembtn, itembtn_back)
        bot.send_message(message.chat.id, "Оберіть наступну дію", reply_markup=markup)

    if message.text == ("Мариновані\n"
                        "огірки \U0001F952"):
        bot.send_message(
        message.chat.id,
        "<b>Інгредієнти:\n</b>"
        "огірки\n"
        "листя хрону\n"
        "кріп із парасольками\n"
        "часник\n"
        "чорний перець горошок\n"
        "листя смородини\n"
        "листя вишні\n\n"
        "<b>Маринад на 1 літр води:</b>\n"
        "вода - 1 л.\n"
        "цукор - 100 г.\n"
        "оцет - 120 мл.\n"
        "сіль - 1 ст.л.",
        parse_mode="HTML"
    )
        
        cucumber_photo = open("bot_project\IMG_6239.JPG", "rb")
        bot.send_photo(message.chat.id, cucumber_photo)
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn = telebot.types.KeyboardButton("Розрахунок маринаду для огірків")
        itembtn_back = telebot.types.KeyboardButton("Назад до меню \U000021A9")
        markup.row(itembtn, itembtn_back)
        bot.send_message(message.chat.id, "Оберіть наступну дію", reply_markup=markup)

    if message.text == "Назад до меню \U000021A9":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = telebot.types.KeyboardButton("Мариновані\n" 
                                                "помідори \U0001F345")
        itembtn2 = telebot.types.KeyboardButton("Мариновані\n"
                                                "огірки \U0001F952")
        markup.row(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Виберіть рецепт із меню \U0001F447", reply_markup=markup)

    if message.text == "Розрахунок маринаду для огірків":
        bot.send_message(
            message.chat.id,
            "<b>Для визначення кількості маринаду\n"
            "виконайте наступні дії:</b>\n"
            "- наповніть банки огірками\n"
            "- візьміть мірну тару і наповніть її окропом\n" 
            "- залийте всі банки окропом та вирахуйте загальну кількість рідини",
            parse_mode="HTML"   
        )
        markup = telebot.types.ForceReply()
        send_value = bot.send_message(
                        message.chat.id,
                        "Введіть в поле 'Повідомлення' отриману "
                        "кількість рідини цифрою \U0001F447",
                        reply_markup=markup
                    )
        bot.register_next_step_handler(send_value, calculate_cucmber_marinade)

    if message.text == "Розрахунок маринаду для помідорів":
        bot.send_message(
            message.chat.id,
            "<b>Для визначення кількості маринаду\n"
            "виконайте наступні дії:</b>\n"
            "- наповніть банки помідорами\n"
            "- візьміть мірну тару і наповніть її окропом\n" 
            "- залийте всі банки окропом та вирахуйте загальну кількість рідини",
            parse_mode="HTML"   
        )
        markup = telebot.types.ForceReply()
        send_value = bot.send_message(
                        message.chat.id,
                        "Введіть в поле 'Повідомлення' отриману "
                        "кількість рідини цифрою \U0001F447",
                        reply_markup=markup
                    )
        bot.register_next_step_handler(send_value, calculate_tomato_marinade)
        
@bot.message_handler(func = lambda message: message.text == "Розрахунок маринаду для огірків")
def calculate_cucmber_marinade(message):
    try:
        bot.send_message(
            message.chat.id,
            f"<b>Маринад на {message.text} л. води:</b>\n"
            f"{calculate.get_cucumber_marinade(float('.'.join((message.text).split(','))))}",
            parse_mode="HTML"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Для розрахунку використовуйте тільки цифри."
        )

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn = telebot.types.KeyboardButton("Розрахунок маринаду для огірків")
    itembtn_back = telebot.types.KeyboardButton("Назад до меню \U000021A9")
    markup.row(itembtn, itembtn_back)
    bot.send_message(message.chat.id, "Оберіть наступну дію", reply_markup=markup)

@bot.message_handler(func = lambda message: message.text == "Розрахунок маринаду для помідорів")
def calculate_tomato_marinade(message):
    try:
        bot.send_message(
            message.chat.id,
            f"<b>Маринад на {message.text} л. води:</b>\n"
            f"{calculate.get_tomato_marinade(float('.'.join((message.text).split(','))))}",
            parse_mode="HTML"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Для розрахунку використовуйте тільки цифри."
        )

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn = telebot.types.KeyboardButton("Розрахунок маринаду для помідорів")
    itembtn_back = telebot.types.KeyboardButton("Назад до меню \U000021A9")
    markup.row(itembtn, itembtn_back)
    bot.send_message(message.chat.id, "Оберіть наступну дію", reply_markup=markup)


bot.polling(non_stop=True)
