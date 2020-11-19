import telebot
import config
import random
import datetime
import schedule
import time
from select_from_db import query_name
from select_from_db import query_random_congrats
from select_from_db import getAllPersons

bot = telebot.TeleBot(config.token)

def get_full_congrat():
    name = query_name()
    names = list(name)


    # date_time_obj = datetime.datetime.strptime(s[0][2], '%Y-%m-%d %H:%M:%S.%f')
    # print(date_time_obj)

    x = datetime.datetime.now()
    print(x.strftime('%m'))
    congratulation = query_random_congrats()
    congratulations = list(congratulation)
    full_congrat = name + congratulation
    # for n in names:
    #     sendCongratToPerson(n, congratulations)

    #sendCongratToPerson(name, congratulations)
    #congrat_str = '_'.join(full_congrat)
    #print(full_congrat)
    #return full_congrat

def sendCongratToPerson(message, names):
    y = query_random_congrats()

    for name in names:
        congrat = getRandomCongrat(y)
        text = getCongratText(name[1], congrat[0])
        bot.send_message(message.chat.id, text)

def getCongratText(name, congrat):
    return 'С днем рождения, ' + name + '!\n' + congrat

def getRandomCongrat(congratulations):
    return random.choice(congratulations)

def getTodayBirthdays(persons):
    todayFullDate = datetime.datetime.now()
    todayDate = todayFullDate.strftime('%d')
    todayMonth = todayFullDate.strftime('%m')

    hasByrthdayPersons = []

    for person in persons:
        if((person[2].strftime('%d') == todayDate) & (person[2].strftime('%m') == todayMonth)):
            hasByrthdayPersons.append(person)

    return hasByrthdayPersons


@bot.message_handler(content_types=['text'])
def test_echo(message):
    persons = getAllPersons()
    while True:
        i = getTodayBirthdays(persons)
        if(len(i) > 0):
            sendCongratToPerson(message, i)
        else:
            continue
        time.sleep(10)

# RUN
bot.polling(none_stop=True)

# if __name__ == '__main__':
#     get_full_congrat()
