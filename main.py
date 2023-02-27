import telebot

bot = telebot.TeleBot('6256136945:AAEtp7h-ChfPzmiTpzREy1h7VkTvtVXgOqA')
bot.user_data = {}
# Обработчик старта
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем и отправляем сообщение с инлайн-кнопками
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('💸Выгодная ипотека', callback_data='topic1'))
    markup.add(telebot.types.InlineKeyboardButton('🌇Подбор по новостройкам', callback_data='topic2'))
    markup.add(telebot.types.InlineKeyboardButton('💼Страхование ипотеки', callback_data='topic3'))
    markup.add(telebot.types.InlineKeyboardButton('🌃Покупка на вторичном рынке', callback_data='topic4'))
    bot.send_message(chat_id=message.chat.id, text='Здравствуйте!  \nВыберите интересующую вас тему:  ', reply_markup=markup)

# Обработчик нажатия на инлайн-кнопку
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'topic1':
        # Обработка выбора темы 1
        bot.send_message(chat_id=call.message.chat.id, text='Ваше ФИО?')
        # Сохраняем ответ на первый вопрос
        bot.user_data[call.message.chat.id] = {'topic': 1, 'q1': call.message.message_id, 'a1': None, 'q2': None, 'a2': None,'q3': None, 'a3': None, 'q4': None, 'a4': None,'q5': None, 'a5': None,'q6': None, 'a6': None,'q7': None, 'a7': None,'q8': None, 'a8': None,'q9': None, 'a9': None,'q10': None, 'a10': None,'q11': None, 'a11': None}
        # Добавляем обработчик ответа на первый вопрос
        bot.register_next_step_handler_by_chat_id(chat_id=call.message.chat.id, callback=handle_answer_topic1_q1)
    elif call.data == 'topic2':
        # Обработка выбора темы 2
        bot.send_message(chat_id=call.message.chat.id, text='Ваше ФИО?')
        # Сохраняем ответ на первый вопрос
        bot.user_data[call.message.chat.id] = {'topic': 2, 'q1': call.message.message_id, 'a1': None, 'q2': None, 'a2': None, 'q3': None, 'a3': None, 'q4': None, 'a4': None,'q5': None, 'a5': None,'q6': None, 'a6': None,'q7': None, 'a7': None,'q8': None, 'a8': None,'q9': None, 'a9': None,'q10': None, 'a10': None,'q11': None, 'a11': None,'q12': None, 'a12': None}
        # Добавляем обработчик ответа на первый вопрос
        bot.register_next_step_handler_by_chat_id(chat_id=call.message.chat.id, callback=handle_answer_topic2_q1)
    elif call.data == 'topic3':
        # Обработка выбора темы 3
        bot.send_message(chat_id=call.message.chat.id, text='Ваше ФИО?')
        # Сохраняем ответ на первый вопрос
        bot.user_data[call.message.chat.id] = {'topic': 3, 'q1': call.message.message_id, 'a1': None, 'q2': None, 'a2': None,'q3': None, 'a3': None, 'q4': None, 'a4': None,'q5': None, 'a5': None,'q6': None, 'a6': None,'q7': None, 'a7': None}
        # Добавляем обработчик ответа на первый вопрос
        bot.register_next_step_handler_by_chat_id(chat_id=call.message.chat.id, callback=handle_answer_topic3_q1)
    elif call.data == 'topic4':
        # Обработка выбора темы 4
        bot.send_message(chat_id=call.message.chat.id, text='Ваше ФИО?')
        # Сохраняем ответ на первый вопрос
        bot.user_data[call.message.chat.id] = {'topic': 4, 'q1': call.message.message_id, 'a1': None, 'q2': None, 'a2': None,'q3': None, 'a3': None, 'q4': None, 'a4': None,'q5': None, 'a5': None,'q6': None, 'a6': None,'q7': None, 'a7': None,'q8': None, 'a8': None,'q9': None, 'a9': None,'q10': None, 'a10': None,'q11': None, 'a11': None,'q12': None, 'a12': None}
        # Добавляем обработчик ответа на первый вопрос
        bot.register_next_step_handler_by_chat_id(chat_id=call.message.chat.id, callback=handle_answer_topic4_q1)


###################################################
#  Первая тема вопросов  (блоки одинаковы)        #
###################################################
# Обработчик ответа на первый вопрос по теме 1
def handle_answer_topic1_q1(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Ваш телефон?')
    # Сохраняем ответ на первый вопрос
    bot.user_data[message.chat.id]['a1'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q2)

    # Обработчик ответа на первый вопрос по теме 1
def handle_answer_topic1_q2(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Город?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a2'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q3)


def handle_answer_topic1_q3(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Дата Вашего рождения?')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a3'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q4)

def handle_answer_topic1_q4(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Ваше семейное положение?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a4'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q5)


def handle_answer_topic1_q5(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Есть ли у Вас дети? Если есть, то какого года рождения?')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a5'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q6)

def handle_answer_topic1_q6(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Вы работаете официально?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a6'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q7)


def handle_answer_topic1_q7(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Были ли у Вас просрочки по кредитам? ')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a7'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q8)

def handle_answer_topic1_q8(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Есть ли у вас задолженности в ФССП (приставы)?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a8'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q9)


def handle_answer_topic1_q9(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Что планируете приобрести?')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a9'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q10)

def handle_answer_topic1_q10(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Напишите свои пожелания')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a10'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic1_q11)

        # Обработчик ответа на Второй вопрос по теме 1
def handle_answer_topic1_q11(message):
            # Отправляем сообщение с благодарностью
    bot.send_message(chat_id=message.chat.id, text='Спасибо за ваши ответы, с вами свяжется ваш персональный менеджер!')
            # Сохраняем ответ на последний вопрос
    bot.user_data[message.chat.id]['a11'] = message.text
            # Отправляем ответы на вопросы в группу
    topic_data = bot.user_data[message.chat.id]
    topic = f'Тема {topic_data["topic"]} : 💸Выгодная ипотека '
    answer1 = f'ФИО: {topic_data["a1"]}'
    answer2 = f'Тел: {topic_data["a2"]}'
    answer3 = f'Город: {topic_data["a3"]}'
    answer4 = f'Дата рождения: {topic_data["a4"]}'
    answer5 = f'Семейное положение: {topic_data["a5"]}'
    answer6 = f'Дети - год рождения: {topic_data["a6"]}'
    answer7 = f'Работа официальная?: {topic_data["a7"]}'
    answer8 = f'Просрочки по кредитам?: {topic_data["a8"]}'
    answer9 = f'Задолженности в ФССП: {topic_data["a9"]}'
    answer10 = f'Что планируете приобрести: {topic_data["a10"]}'
    answer11 = f'Напишите свои пожелания: {topic_data["a11"]}'
    bot.send_message(chat_id='-840355519',
    text=f'{topic}\n{answer1}\n{answer2}\n{answer3}\n{answer4}\n{answer5}\n{answer6}\n{answer7}\n{answer8}\n{answer9}\n{answer10}\n{answer11}')
            # Очищаем данные пользователя
    bot.user_data[message.chat.id] = {}


###################################################
#  Вторая тема вопросов  (блоки одинаковы)        #
###################################################
# Обработчик ответа на первый вопрос по теме 1
def handle_answer_topic2_q1(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Ваш телефон?')
    # Сохраняем ответ на первый вопрос
    bot.user_data[message.chat.id]['a1'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q2)

    # Обработчик ответа на первый вопрос по теме 1
def handle_answer_topic2_q2(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Дата Вашего рождения?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a2'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q3)


def handle_answer_topic2_q3(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите город приобретения?')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a3'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q4)

def handle_answer_topic2_q4(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите размер своего первоначального взноса:')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a4'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q5)


def handle_answer_topic2_q5(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Вы в браке?')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a5'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q6)

def handle_answer_topic2_q6(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Есть ли у вас дети? Какого года рождения дети? ')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a6'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q7)


def handle_answer_topic2_q7(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Сколько комнатную квартиру планируете приобрести?')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a7'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q8)

def handle_answer_topic2_q8(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Желаемые этажи?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a8'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q9)


def handle_answer_topic2_q9(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Вы работаете официально? ')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a9'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q10)

def handle_answer_topic2_q10(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Средний размер вашей заработной платы?')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a10'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q11)

def handle_answer_topic2_q11(message):
            # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Были ли у вас просроченные платежи по кредитам?')
            # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a11'] = message.text
            # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic2_q12)


        # Обработчик ответа на последний вопрос по теме 2
def handle_answer_topic2_q12(message):
            # Отправляем сообщение с благодарностью
    bot.send_message(chat_id=message.chat.id, text='Спасибо за ваши ответы, с вами свяжется ваш персональный менеджер!')
            # Сохраняем ответ на последний вопрос
    bot.user_data[message.chat.id]['a12'] = message.text
            # Отправляем ответы на вопросы в группу
    topic_data = bot.user_data[message.chat.id]
    topic = f'Тема {topic_data["topic"]} : 🌇Подбор по новостройкам '
    answer1 = f'ФИО: {topic_data["a1"]}'
    answer2 = f'Тел: {topic_data["a2"]}'
    answer3 = f'Дата рождения: {topic_data["a3"]}'
    answer4 = f'Город приобретения: {topic_data["a4"]}'
    answer5 = f'Размер взноса: {topic_data["a5"]}'
    answer6 = f'Семейное положение: {topic_data["a6"]}'
    answer7 = f'Дети - год рождения: {topic_data["a7"]}'
    answer8 = f'Комнаты : {topic_data["a8"]}'
    answer9 = f'Этажи: {topic_data["a9"]}'
    answer10 = f'Официально работает? : {topic_data["a10"]}'
    answer11 = f'Ср. Размер зарплаты: {topic_data["a11"]}'
    answer12 = f'Просрочки были?: {topic_data["a12"]}'
    bot.send_message(chat_id='-840355519',text=f'{topic}\n{answer1}\n{answer2}\n{answer3}\n{answer4}\n{answer5}\n{answer6}\n{answer7}\n{answer8}\n{answer9}\n{answer10}\n{answer11}\n{answer12}')
            # Очищаем данные пользователя
    bot.user_data[message.chat.id] = {}

###################################################
#  Третья тема вопросов  (блоки одинаковы)        #
###################################################
# Обработчик ответа на первый вопрос по теме 1
def handle_answer_topic3_q1(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Ваш телефон?')
    # Сохраняем ответ на первый вопрос
    bot.user_data[message.chat.id]['a1'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic3_q2)

    # Обработчик ответа на первый вопрос по теме 1
def handle_answer_topic3_q2(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите ваш город:')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a2'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic3_q3)


def handle_answer_topic3_q3(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите банк, в котором ипотека:')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a3'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic3_q4)

def handle_answer_topic3_q4(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите остаток долга на сегодняшний день:')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a4'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic3_q5)


def handle_answer_topic3_q5(message):
    # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите возраст основного заемщика и пол:')
    # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a5'] = message.text
    # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic3_q6)

def handle_answer_topic3_q6(message):
        # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Скажите, был ли созаемщик? Укажите Возраст Созаемщика? ')
        # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a6'] = message.text
        # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic3_q7)



        # Обработчик ответа на последний вопрос по теме 2
def handle_answer_topic3_q7(message):
            # Отправляем сообщение с благодарностью
    bot.send_message(chat_id=message.chat.id, text='Спасибо за ваши ответы, с вами свяжется ваш персональный менеджер!')
            # Сохраняем ответ на последний вопрос
    bot.user_data[message.chat.id]['a7'] = message.text
            # Отправляем ответы на вопросы в группу
    topic_data = bot.user_data[message.chat.id]
    topic = f'Тема {topic_data["topic"]} : 💼Страхование ипотеки '
    answer1 = f'ФИО: {topic_data["a1"]}'
    answer2 = f'Тел: {topic_data["a2"]}'
    answer3 = f'Город: {topic_data["a3"]}'
    answer4 = f'Банк: {topic_data["a4"]}'
    answer5 = f'Остаток долга: {topic_data["a5"]}'
    answer6 = f'Возраст и пол основного заемщика: {topic_data["a6"]}'
    answer7 = f'Созаемщик? Его пол?: {topic_data["a7"]}'
    bot.send_message(chat_id='-840355519',text=f'{topic}\n{answer1}\n{answer2}\n{answer3}\n{answer4}\n{answer5}\n{answer6}\n{answer7}')
            # Очищаем данные пользователя
    bot.user_data[message.chat.id] = {}
###################################################
#  Четвертая тема вопросов  (блоки одинаковы)     #
###################################################

def handle_answer_topic4_q1(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Ваш телефон?')
                # Сохраняем ответ на первый вопрос
    bot.user_data[message.chat.id]['a1'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q2)

                # Обработчик ответа на первый вопрос по теме 1

def handle_answer_topic4_q2(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Дата Вашего рождения?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a2'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q3)

def handle_answer_topic4_q3(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите город приобретения?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a3'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q4)

def handle_answer_topic4_q4(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Укажите размер своего первоначального взноса:')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a4'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q5)

def handle_answer_topic4_q5(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Вы в браке?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a5'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q6)

def handle_answer_topic4_q6(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Есть ли у вас дети? Какого года рождения дети? ')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a6'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q7)

def handle_answer_topic4_q7(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Сколько комнатную квартиру планируете приобрести?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a7'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q8)

def handle_answer_topic4_q8(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Желаемые этажи?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a8'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q9)

def handle_answer_topic4_q9(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Вы работаете официально? ')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a9'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q10)

def handle_answer_topic4_q10(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Средний размер вашей заработной платы?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a10'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q11)

def handle_answer_topic4_q11(message):
                # Отправляем второй вопрос
    bot.send_message(chat_id=message.chat.id, text='Были ли у вас просроченные платежи по кредитам?')
                # Сохраняем ответ на второй вопрос
    bot.user_data[message.chat.id]['a11'] = message.text
                # Добавляем обработчик ответа на второй вопрос
    bot.register_next_step_handler_by_chat_id(chat_id=message.chat.id, callback=handle_answer_topic4_q12)

            # Обработчик ответа на последний вопрос по теме 2
def handle_answer_topic4_q12(message):
                # Отправляем сообщение с благодарностью
    bot.send_message(chat_id=message.chat.id,text='Спасибо за ваши ответы, с вами свяжется ваш персональный менеджер!')
                # Сохраняем ответ на последний вопрос
    bot.user_data[message.chat.id]['a12'] = message.text
                # Отправляем ответы на вопросы в группу
    topic_data = bot.user_data[message.chat.id]
    topic = f'Тема {topic_data["topic"]} : 🌃Покупка квартиры на вторичном рынке '
    answer1 = f'ФИО: {topic_data["a1"]}'
    answer2 = f'Тел: {topic_data["a2"]}'
    answer3 = f'Дата рождения: {topic_data["a3"]}'
    answer4 = f'Город приобретения: {topic_data["a4"]}'
    answer5 = f'Размер взноса: {topic_data["a5"]}'
    answer6 = f'Семейное положение: {topic_data["a6"]}'
    answer7 = f'Дети - год рождения: {topic_data["a7"]}'
    answer8 = f'Комнаты : {topic_data["a8"]}'
    answer9 = f'Этажи: {topic_data["a9"]}'
    answer10 = f'Официально работает? : {topic_data["a10"]}'
    answer11 = f'Ср. Размер зарплаты: {topic_data["a11"]}'
    answer12 = f'Просрочки были?: {topic_data["a12"]}'
    bot.send_message(chat_id='-840355519',text=f'{topic}\n{answer1}\n{answer2}\n{answer3}\n{answer4}\n{answer5}\n{answer6}\n{answer7}\n{answer8}\n{answer9}\n{answer10}\n{answer11}\n{answer12}')
                # Очищаем данные пользователя
    bot.user_data[message.chat.id] = {}




    # Запускаем бота
bot.polling(none_stop=True)

