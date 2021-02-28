import time
import speech_recognition as sr
import pokemon

# RASPBERRY PI SETUP
import board
import digitalio
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)

lcd_columns = 16
lcd_rows = 2

import adafruit_character_lcd.character_lcd as characterlcd
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# SPEECH TO TEXT
r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        entry = pokemon.pokedex[text]
        print(entry.name + "\n" + entry.desc)
        lcd.message = entry.name + "\n" + entry.desc
    except:
        print("voice not recognized")
