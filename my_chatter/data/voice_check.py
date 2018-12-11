import pyttsx3

mine = pyttsx3.init()
#voice = mine.getProperty('voice')
voices = mine.getProperty('voices')
print(voices)
mine.setProperty('voice', voices[1])
rate = mine.getProperty('rate')
print(rate)
volume = mine.getProperty('volume')
print(volume)