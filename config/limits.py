
import gtts
from playsound import playsound
import random
import os


def speak(phrase):
    try:
        info = gtts.gTTS(phrase, lang='pt-br')
        info.save('phrase.mp3')
        playsound('phrase.mp3')
        os.remove('phrase.mp3')
    except Exception:
        pass


def get_phrase(array):
    length = len(array)
    if length == 1:
        return array[length - 1]
    lengthRandom = random.randrange(0, length)
    return array[lengthRandom]
