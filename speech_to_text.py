import pyfirmata
import time
import speech_recognition as sr

board = pyfirmata.Arduino("/dev/cu.usbmodem14201")

# BLINK PROGRAM
# while True:
#     board.digital[13].write(1)
#     time.sleep(1)
#     board.digital[13].write(0)
#     time.sleep(1)

# SPEECH TO TEXT
r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
    except:
        print("voice not recognized")
