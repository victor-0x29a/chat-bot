
import gtts
from playsound import playsound
import random
import os

def speak(frase):
    try:
        info = gtts.gTTS(frase,lang='pt-br')
        info.save('phrase.mp3')
        playsound('phrase.mp3')
        os.remove('phrase.mp3')
    except Exception as error:
        pass


def getPhrase(array):
    tam = len(array)
    if tam == 1:
        return array[tam - 1]
    tamRandom = random.randrange(0, tam)
    return array[tamRandom]
