import pyttsx3
import time

engine = pyttsx3.init()
user_time = input('''Enter time to set timer?:
        hint:(if System clock is 24 hours wirte : 13:00
        else write : 01:24 )

Enter? :''')

user_msg = input("Any Label you want?(message) :")
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-10)
while True:
    if time.strftime("%H:%M") == user_time:
        if user_msg is None:
            engine.say('Do your work, time is '+ time.strftime("%H:%M"))
            engine.runAndWait()
            break
        else:
            engine.say('Time is : '+time.strftime("%H:%M"))
            engine.runAndWait()
            engine.say(user_msg)
            engine.runAndWait()
            break

