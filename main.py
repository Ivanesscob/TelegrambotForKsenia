
import telebot
from telebot import types

bot = telebot.TeleBot('6776647450:AAFLQAhDQ79toGeumsLOGeTNb5iaU_XevLc')

@bot.message_handler(commands=["start"])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    rmk.add(types.KeyboardButton('Атлант'), types.KeyboardButton('Алые паруса'), types.KeyboardButton('Прожектор'))

    msg = bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name}</b>\nВыбери комманду:', parse_mode='html', reply_markup=rmk)
    bot.register_next_step_handler(msg, user_answer)

def user_answer(message):
    if message.text == "Атлант":
        bot.send_message(message.chat.id, 'Рыба-карась, игра началась!')
        video1 = open('IMG_1431.MOV','rb')
        bot.send_video(message.chat.id, video1)
        bot.send_message(message.chat.id,
                         'Катя книжку слушает,\nКоля кашку кушает,\nС горки катится Кирюша,\nКисти с красками у Ксюши.')
        bot.send_message(message.chat.id, '60.016646, 30.433762')
        bot.send_message(message.chat.id, 'При неверном выборе команды напишите /start')
        msg = bot.send_message(message.chat.id, 'Пришлите фото ответа:')
        bot.register_next_step_handler(msg, atlant_ph1)
    elif message.text == "Алые паруса":
        bot.send_message(message.chat.id, 'Рыба-карась, игра началась!')
        video2= open('IMG_1431.MOV', 'rb')
        bot.send_video(message.chat.id, video2)
        bot.send_message(message.chat.id,
                         'Катя книжку слушает,\nКоля кашку кушает,\nС горки катится Кирюша,\nКисти с красками у Ксюши.')
        bot.send_message(message.chat.id, '60.006957, 30.424239')
        bot.send_message(message.chat.id, 'При неверном выборе команды напишите /start')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, alee_ph1)
    elif message.text == "Прожектор":
        bot.send_message(message.chat.id, 'Рыба-карась, игра началась!')
        video3 = open('IMG_1431.MOV', 'rb')
        bot.send_video(message.chat.id, video3)
        bot.send_message(message.chat.id,'Катя книжку слушает,\nКоля кашку кушает,\nС горки катится Кирюша,\nКисти с красками у Ксюши.')
        bot.send_message(message.chat.id, '60.008378, 30.418114')
        bot.send_message(message.chat.id, 'При неверном выборе команды напишите /start')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, pr_ph1)
    else:
        bot.send_message(message.chat.id, "Нет такой команды!\nНапишите /start")
def atlant_ph1(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, atlant_k)

def pr_ph1(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, pr_k)


def atlant_k(message):
    if message.text == 'Атлант_К':
        bot.send_message(message.chat.id,'Воу-воу! Мы набираем обороты! Машина запущена! Но еще чего-то не хватает?!')
        photo = open('1.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, '60.016646, 30.433762')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, atlant_ph2)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def atlant_ph2(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, atlant_n)

def alee_ph1(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, alee_k)


def atlant_n(message):
    if message.text == 'Атлант_Н':
        bot.send_message(message.chat.id,
                         'Ноги в руки! Это еще не конец, а только середина. Квест продолжается! Силы еще остались?')
        bot.send_message(message.chat.id,f'  &#129398; &#129503; &#129427; &#127757;', parse_mode='html')
        bot.send_message(message.chat.id, '60.011361, 30.427794')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, atlant_ph3)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def atlant_ph3(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, atlant_z)

def atlant_z(message):
    if message.text == 'Атлант_З':
        bot.send_message(message.chat.id,'Бинго! Хорошо идем! А как тебе такое,  Илон Маск?')
        audio = open('12.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        bot.send_message(message.chat.id, '60.008327, 30.427522')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, atlant_ph4)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def atlant_ph4(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, atlant_o)

def atlant_o(message):
    if message.text == 'Атлант_О':
        bot.send_message(message.chat.id,'А вы приятно удивляете! Можно уже вас отправлять на игру "Что?Где?Когда?". Осталось выбрать, кто из вас Друзь?\nЭто оставим на потом! А игра продолжается!')
        bot.send_message(message.chat.id, '.- .. ... - , .- --.. -... -.- .- , .- .-. -... ..- --..')
        bot.send_message(message.chat.id, '60.007482, 30.435976')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, atlant_ph5)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def atlant_ph5(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, atlant_a)

def atlant_a(message):
    if message.text == 'Атлант_А':
        bot.send_message(message.chat.id,'Продолжаем разговор?! Сколько букв собрали?')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, atlant_ph6)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def atlant_ph6(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, atlant_5)

def atlant_5(message):
    if message.text == '5':
        bot.send_message(message.chat.id, 'Бегом туда! Вас уже ждут!')
        bot.send_message(message.chat.id, '60.013927, 30.434537')
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')

def alee_k(message):
    if message.text == 'Алые паруса_К':
        bot.send_message(message.chat.id, 'Воу-воу! Мы набираем обороты! Машина запущена! Но еще чего-то не хватает?!')
        photo = open('1.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, '60.012259, 30.425829')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, alee_ph2)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def alee_ph2(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, alee_n)


def alee_n(message):
    if message.text == 'Алые паруса_Н':
        bot.send_message(message.chat.id, 'Ноги в руки! Это еще не конец, а только середина. Квест продолжается! Силы еще остались?')
        bot.send_message(message.chat.id,f'  &#129398; &#129503; &#129427; &#127757;', parse_mode='html')
        bot.send_message(message.chat.id, '60.009691, 30.425731')
        msg = bot.send_message(message.chat.id, 'Пришлите фото ответа:')
        bot.register_next_step_handler(msg, alee_ph3)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def alee_ph3(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, alee_z)

def alee_z(message):
    if message.text == 'Алые паруса_З':
        bot.send_message(message.chat.id,'Бинго! Хорошо идем! А как тебе такое,  Илон Маск?')
        audio = open('12.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        bot.send_message(message.chat.id, '60.015358, 30.429929')
        msg = bot.send_message(message.chat.id, 'Пришлите фото ответа:')
        bot.register_next_step_handler(msg, alee_ph4)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def alee_ph4(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, alee_o)

def alee_o(message):
    if message.text == 'Алые паруса_О':
        bot.send_message(message.chat.id,'А вы приятно удивляете! Можно уже вас отправлять на игру "Что?Где?Когда?". Осталось выбрать, кто из вас Друзь?\nЭто оставим на потом! А игра продолжается!')
        bot.send_message(message.chat.id, '.- .. ... - , .- --.. -... -.- .- , .- .-. -... ..- --..')
        bot.send_message(message.chat.id, '60.013159, 30.430002')
        msg = bot.send_message(message.chat.id, 'Пришлите фото ответа:')
        bot.register_next_step_handler(msg, alee_ph5)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def alee_ph5(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, alee_a)
def alee_a(message):
    if message.text == 'Алые паруса_А':
        bot.send_message(message.chat.id,'Продолжаем разговор?! Сколько букв собрали?')
        msg = bot.send_message(message.chat.id, 'Пришлите фото ответа:')
        bot.register_next_step_handler(msg, alee_ph6)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def alee_ph6(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, alee_5)
def alee_5(message):
    if message.text == '5':
        bot.send_message(message.chat.id, 'Бегом туда! Вас уже ждут!')
        bot.send_message(message.chat.id, '60.013927, 30.434537')
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')


def pr_k(message):
    if message.text == 'Прожектор_К':
        bot.send_message(message.chat.id,
                         'Воу-воу! Мы набираем обороты! Машина запущена! Но еще чего-то не хватает?!')
        photo = open('1.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, '60.012354, 30.418772')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, pr_ph2)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def pr_ph2(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, pr_n)
def pr_n(message):
    if message.text == 'Прожектор_Н':
        bot.send_message(message.chat.id,
                         'Ноги в руки! Это еще не конец, а только середина. Квест продолжается! Силы еще остались?')
        bot.send_message(message.chat.id,f'  &#129398; &#129503; &#129427; &#127757;', parse_mode='html')
        bot.send_message(message.chat.id, '60.011216, 30.420464')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, pr_ph3)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def pr_ph3(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, pr_z)
def pr_z(message):
    if message.text == 'Прожектор_З':
        bot.send_message(message.chat.id, 'Бинго! Хорошо идем! А как тебе такое,  Илон Маск?')
        audio = open('12.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        bot.send_message(message.chat.id, '60.010431, 30.426654')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, pr_ph4)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def pr_ph4(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, pr_o)
def pr_o(message):
    if message.text == 'Прожектор_О':
        bot.send_message(message.chat.id,
                         'А вы приятно удивляете! Можно уже вас отправлять на игру "Что?Где?Когда?". Осталось выбрать, кто из вас Друзь?\nЭто оставим на потом! А игра продолжается!')
        bot.send_message(message.chat.id, '.- .. ... - , .- --.. -... -.- .- , .- .-. -... ..- --..')
        bot.send_message(message.chat.id, '60.013026, 30.429926')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, pr_ph5)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def pr_ph5(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, pr_a)
def pr_a(message):
    if message.text == 'Прожектор_А':
        bot.send_message(message.chat.id, 'Продолжаем разговор?! Сколько букв собрали?')
        msg = bot.send_message(message.chat.id, 'Пришли фото ответа:')
        bot.register_next_step_handler(msg, pr_ph6)
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
def pr_ph6(message):
    msg = bot.send_message(message.chat.id, 'Пришли ответ:')
    bot.register_next_step_handler(msg, pr_5)
def pr_5(message):
    if message.text == '5':
        bot.send_message(message.chat.id, 'Бегом туда! Вас уже ждут!')
        bot.send_message(message.chat.id, '60.013927, 30.434537')
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, введи /start и поробуй снова!')
bot.infinity_polling()
