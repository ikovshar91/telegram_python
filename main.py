from telebot import types

import telebot

def main():
    bot = telebot.TeleBot('5163229580:AAEZ2DQzqFbPn3tQ38zJcCtKX6pEjoKLcsk')

    name = ""
    surname = ""
    age = 0

    print('Бот запущен')

    @bot.message_handler(content_types=['text'])
    def start(message):
        if message.text == '/reg':
            bot.send_message(message.from_user.id, "Как тебя зовут?");
            bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
        else:
            bot.send_message(message.from_user.id, 'Напиши /reg');

    def get_name(message):  # получаем фамилию
        global name
        name = message.text
        bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
        bot.register_next_step_handler(message, get_surname)

    def get_surname(message):
        global surname
        surname = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)

    def get_age(message):
        global age
        global surname
        global name

        age = int(message.text)  # проверяем, что возраст введен корректно
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
            ... # код сохранения данных, или их обработки
            bot.send_message(call.message.chat.id, 'Запомню : )');
        elif call.data == "no":
            ...  # переспрашиваем

    # Запускаем бота
    bot.polling(none_stop=True, interval=0)

    print('Бот остановлен')


if __name__ == '__main__':
    main()
