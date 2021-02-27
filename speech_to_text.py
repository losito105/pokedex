import pyfirmata
import time
import speech_recognition as sr
import pokemon

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
        entry = pokemon.pokedex[text]
        # TODO: print entry.name and entry.desc to LCD module
    except:
        print("voice not recognized")
