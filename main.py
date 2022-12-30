import telebot
import os
from threading import Thread
import time
import subprocess
import json




try:
    toke_file = open("token.txt", 'r')
    token = toke_file.read()
except:
    print("Token file not found")
    exit()


cmd = "termux-battery-status"

bot = telebot.TeleBot(token)

def check_db():
    try:
        if os.path.exists("DB.txt") == False:
            print("User Fb not exist")
            return "NE"
        else:
            print("All good DB exists")
            return "200"
    except:
        print("Unknown Error:")

def add_user(username):

    try:
        db = open("DB.txt", 'a')

        #wiriting username

        try:

            usernameW = username + "\n"
            db.write(usernameW)



            db.close()
            print("User added: " + username)
        except:
            print("Adding user error")


    except:
        print("DB Error 1")


@bot.message_handler(commands=["link"])
def link_user(message):
    chat_id = message.chat.id
    add_user(str(chat_id))

    bot.send_message(message.chat.id, "Тепер коли пропадає світло тобі будуть приходити смс")


def GET_STATUS():
    print("Geting status")

    result_raw = subprocess.Popen(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE,)
                                 #env=os.environ)

    result = result_raw.stdout.read() + result_raw.stderr.read()
    print(result)

    response_json_orig = result


    response_json_raw = """{
  "health": "GOOD",
  "percentage": 93,
  "plugged": "UNPLUGGED",
  "status": "DISCHARGING",
  "temperature": 33.900001525878906,
  "current": 322723
}"""
    response_json = json.loads(response_json_orig)
    print(response_json["plugged"])

    temper = str(response_json['temperature'])
    temper = temper[0:4]

    if response_json['plugged'] == "UNPLUGGED":
        return "🚨 220 OFF" + " | " + "TEMP: " + str(temper) + " | " + "POWER: " + str(response_json['percentage']) + "%"
    if response_json['plugged'] == "PLUGGED_AC":
        return "💡 220 ON" + " | " + "TEMP: " + str(temper) + " | " + "POWER: " + str(response_json['percentage']) + "%"


@bot.message_handler(commands=["status"])
def check_alarm(message):
    
    
    bot.send_message(message.chat.id, str(GET_STATUS()))
    



def alarm_hendler():

    alarm_hendler_data = True

    return alarm_hendler_data

def alarm():
    print("WAITING TO ALARM")

    alarm = True
    STATUS = "POWER ON"
    last_status = "POWER ON"

    while True:
        print("Waiting for alarm...")


        if alarm == True:



            STATUS = GET_STATUS()
            print("Status = " + STATUS)


            #spam alarm

            count = 0
            try:

                if True == True:
                    print("STATUS CHANGED" + str(STATUS))
                    last_status = "POWER OFF"
                    with open("DB.txt") as fp:
                        Lines = fp.readlines()
                        for line in Lines:
                            count += 1                                #print("Line{}: {}".format(count, line.strip()))
                            print("Sending alarm to " + line.strip())
                            try:
                                bot.send_message(line.strip(), STATUS)
                            except:
                                print("NETWORK ERROR")
                


            except:
                print("ERROR")




        time.sleep(1800) # normal 1200






#@message_handlers(command=["Підписати"])
def linkbot():
    print("hello world!")

#bot.polling()



if __name__ ==  '__main__':
    print("starting bot")
    print("Cheacking database...")
    if check_db() == "NE":
        print("FAILED")
        print("Cretae DB.txt")
        exit()
    elif check_db() == "200":
        print("GOOD")
    print("Starting alarm thread...")
    # alrm thread

    alarm_process = Thread(target=alarm, args=())
    alarm_process.start()
    # alrm thread

    #print("TESTING")
    #add_user("2454345434554324")
    #time.sleep(2)
    #add_user("12345678")

    #print('Start poolig bot')
    bot.polling(True)

    #GET_STATUS()
