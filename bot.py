import pyautogui as pag
import speech_recognition as sr
import sys
import os


exit_list = ['выход','выйди','закройся','выходи','Закройся','Выйди','Выход','Выходи']
tg_open = ['Открой Telegram','Telegram открой','Запусти Telegram','Telegram','Telegram Запусти','Зайди в Telegram']
blitz_open = ['танки','Танки','Танчики','танчики','блиц','Блиц','блитс','Блитс','blitz','Blitz']
r = sr.Recognizer()

def programm_open(task):
    for i in tg_open:
        if task == i:
            os.startfile(r"C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
            break


print("Say something!")
with sr.Microphone() as source:
    while True:
        try:
            audio = r.listen(source)
            task = r.recognize_google(audio,language = 'RU-ru')
            print(task)
            for i in exit_list:
                if task == i:
                    sys.exit()
            programm_open(task)

        except sr.UnknownValueError:
            print("еще раз!")
            continue

# Traceback (most recent call last):
#   File "D:\PYTHON\ATOM\Voice_bot\bot.py", line 12, in <module>
#     task = r.recognize_google(audio,language = 'RU-ru')
#   File "C:\Users\User\AppData\Local\Programs\Python\Python36\lib\site-packages\speech_recognition\__init__.py", line 858, in recognize_google
#     if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError()
# speech_recognition.UnknownValueError


# string = str(pag.position())
# begin = string.find('x')
# end = string.find(',')
# x_place = int(string[(begin+2):end])
#
# # pag.moveTo(x_place,60,duration=1.5)
# # pag.click(x_place,60,duration=2)
# # pag.click(x_place,60)
#
# pag.dragRel(50,200,duration=1,button='left')
# # size()           #gave you the size of the screen
# # position()     #return current position of mouse
# # moveTo(200,0,duration=1.5)     #move the cursor  to (200,0) position  with 1.5 second delay
# # moveRel()          #move the cursor relative to your current position.
# # click(337,46)           #it will click on the position mention there
# # dragRel()              #it will drag the mouse relative to position
# # pyautogui.displayMousePosition()     #gave you the current mouse position but should be done on terminal.
