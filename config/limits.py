
import gtts
from playsound import playsound
import random
import os
urlBase = "http://localhost"
def MinAprendizado():
    return 3;

def indecisive():
    return "Ops! não consegui identificar oque você quer que eu faça, você pode repetir de forma clara?"

def speak(frase):
    try:
        info = gtts.gTTS(frase,lang='pt-br')
        info.save('phrase.mp3')
        playsound('phrase.mp3')
        os.remove('phrase.mp3')
    except Exception as error:
        pass



def execute(url, payload, base):
    if len(base) < 2:
        print("top vei")

def getPhrase(array):
    tam = len(array)
    if tam == 1:
        return array[tam - 1]
    tamRandom = random.randrange(0, tam)
    return array[tamRandom]
