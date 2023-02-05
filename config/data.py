# ID REFERENTE - PALAVRAS QUE VAI PROCURAR NA PERGUNTA - VETORES PARA BUSCAR DADOS DEPOIS
import os
import pyautogui as pt
import time
import math
import random
from .limits import speak, getPhrase

def delay(type):
    if type == "s":
        time.sleep(1.5)
    elif type == "m":
        time.sleep(3)
    elif type == "g":
        time.sleep(4.5)

pathBrave = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
def openUrl(url):
    os.startfile(pathBrave)
    delay("s")
    pt.write(url)
    pt.press("enter")
def openInYoutube(search):
    os.startfile(pathBrave)
    delay("s")
    URL = "youtube.com/results" + "?" + "search_query=" + search.replace("por", "").replace("no", "").replace("youtube", "")
    pt.write(URL)
    pt.press("space")
    pt.press("enter")
def Math(phrase):
    if "*" in phrase:
        operation = phrase.replace(",",".").split(" ")
        for op in operation:
            if op == "*":
                operation.remove("*")
        if len(operation) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            return speak(getPhrase([operation[0] + " vezes " + operation[1] + " deu " + str(float(operation[0]) * float(operation[1])) + ", mande uma mais díficil!", "A operação deu " + str(float(operation[0]) * float(operation[1])) ]))
    if "vezes" in phrase:
        operation = phrase.replace(",",".").split(" ")
        for op in operation:
            if op == "vezes":
                operation.remove("vezes")
        if len(operation) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            return speak(getPhrase([operation[0] + " vezes " + operation[1] + " deu " + str(float(operation[0]) * float(operation[1])) + ", mande uma mais díficil!", "A operação deu " +str(float(operation[0]) * float(operation[1])) ]))
    if "mais" in phrase:
        operation = phrase.replace(",",".").split(" ")
        for op in operation:
            if op == "mais":
                operation.remove("mais")
        if len(operation) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            speak("oi")
            return speak(getPhrase([operation[0] + " mais " + operation[1] + " deu " + str(float(operation[0]) + float(operation[1])) + ", mande uma mais díficil!", "A operação deu " +str(float(operation[0]) + float(operation[1])) ]))
    if "+" in phrase:
        operation = phrase.replace(",",".").split(" ")
        for op in operation:
            if op == "+":
                operation.remove("+")
        if len(operation) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            return speak(getPhrase([str(operation[0]) + " mais " + str(operation[1]) + " deu " + str(float(operation[0]) + float(operation[1])) + ", mande uma mais díficil!", "A operação deu " +str(float(operation[0]) + float(operation[1])) ]))
    if "menos" in phrase:
        operation = phrase.replace(",",".").split(" ")
        for op in operation:
            if op == "menos":
                operation.remove("menos")
        if len(operation) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            return speak(getPhrase([operation[0] + " menos " + operation[1] + " deu " + str(float(operation[0]) - float(operation[1])) + ", mande uma mais díficil!", "A operação deu " + str(float(operation[0]) - float(operation[1])) ]))
    if "-" in phrase:
        operation = phrase.replace(",",".").split(" ")
        for op in operation:
            if op == "-":
                operation.remove("-")
        if len(operation) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            return speak(getPhrase([operation[0] + " menos " + operation[1] + " deu " + str(float(operation[0]) - float(operation[1])) + ", mande uma mais díficil!", "A operação deu " + str(float(operation[0]) - float(operation[1])) ]))
    if "dividido" in phrase:
        operation = phrase.replace(",",".").split(" ")
        newArray = []
        inteiros = [0,1,2,3,4,5,6,7,8,9]
        for obj in operation:
            for i in inteiros:
                if obj[0] == str(i):
                    newArray.append(obj)
        if len(newArray) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            return speak(getPhrase([newArray[0] + " dividido por " + newArray[1] + " deu " + str(float(newArray[0]) / float(newArray[1])) + ", mande uma mais díficil!", "A operação deu " + str(float(newArray[0]) / float(newArray[1])) ]))
    if "%" in phrase:
        operation = phrase.replace(",",".").split(" ")
        newArray = []
        inteiros = [0,1,2,3,4,5,6,7,8,9]
        for obj in operation:
            for i in inteiros:
                if obj[0] == str(i):
                    newArray.append(obj)
        if len(newArray) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            total = (float(newArray[0]) * float(newArray[1])) / 100
            return speak(getPhrase([newArray[0] + " porcento de " + newArray[1] + " deu " + str(total) + ", mande uma mais díficil!", "A operação deu " + str(total) ]))
    if "porcento" in phrase or "porcentos" in phrase:
        operation = phrase.replace(",",".").split(" ")
        newArray = []
        inteiros = [0,1,2,3,4,5,6,7,8,9]
        for obj in operation:
            for i in inteiros:
                if obj[0] == str(i):
                    newArray.append(obj)
        if len(newArray) > 2:
            return speak(getPhrase(["Hummm! não consegui obter o resultado dessa conta, vale lembrar que consigo apenas efetuar cálculos entre X e Y, ou seja, somente de dois valores!", "Eu só consigo efetuar contas sobre dois valores!"]))
        else:
            total = (float(newArray[0]) * float(newArray[1])) / 100
            return speak(getPhrase([newArray[0] + " porcento de " + newArray[1] + " deu " + str(total) + ", mande uma mais díficil!", "A operação deu " + str(total) ]))
    if "raiz" in phrase:
        operation = phrase.replace(",",".").split(" ")
        newArray = []
        inteiros = [0,1,2,3,4,5,6,7,8,9]
        for obj in operation:
            for i in inteiros:
                if obj[0] == str(i):
                    newArray.append(obj)
        if len(newArray) > 1:
            return speak(getPhrase(["Hummm! Para calcular a raiz eu só consigo de um número!", "Eu só consigo efetuar contas sobre um valor!"]))
        else:
            total = math.sqrt(float(newArray[0]))
            return speak(getPhrase(["A raiz de " + newArray[0] + " deu " + str(float("{:.2f}".format(total))) + ", mande uma mais díficil!", "A operação deu " + str(float("{:.2f}".format(total))) ]))
def parNumber(phrase):
    frase = phrase.split(" ")
    newArray = []
    inteiros = [0,1,2,3,4,5,6,7,8,9]
    for obj in frase:
        for i in inteiros:
            if obj[0] == str(i):
                newArray.append(obj)
    if (float(newArray[0]) % 2 )== 0:
        return speak(getPhrase(["Sim o valor " + str(float(newArray[0])) + " é par...", "Sim, ele é par!"]))
    else:
        return speak(getPhrase(["Não, o valor " + str(float(newArray[0])) + " não é par!", "Não, ele não é par!"]))
def generateRandomByStdin(phrase):
    frase = phrase.split(" ")
    newArray = []
    inteiros = [0,1,2,3,4,5,6,7,8,9]
    for obj in frase:
        for i in inteiros:
            if obj[0] == str(i):
                newArray.append(obj)
    maior = 0;
    menor = 0;

    if int(newArray[0]) > int(newArray[1]):
        maior = newArray[0]
        menor = newArray[1]
    else:
        maior = newArray[1]
        menor = newArray[0]
    result = random.randint(int(menor), int(maior))
    return speak(getPhrase([f"Claros, o número sorteado foi {result}", f"O número sorteado entre {menor} e {maior} foi {result}"]))
def PhRaseActions():
        return [{"UUID": 0, "Words": ["ataque","derrube","derruba", "wifi", "canal", "canais", "nos", "banda", "2.4", "redes", "no"], "Actions": {"url": "/wifi/deauther", "vetores": ["canal", "canais"]}, "type": "int", "payload": ["canais"], "response": ["Okay vou atacar!", "Tudo bem, irei atacar agora.", "Opa, claros! Vou iniciar o ataque de deauther!", "Oh, sim, vou atacar...", "Claros, irei atacar todos os sinais de wifi no canal desejado!"],  "action": False},
    {"UUID": 1, "Words": ["oi", "oi," "olá," "olá", "bem", "bem?","tudo","certo","certo?", "você", "opa", "vc", "?", "vc?"], "Actions": {"url": "", "vetores": []}, "type": "str", "payload": [], "response": ["Olá, posso te ajudar com alguma coisa?", "Oi, eu sou uma assistente focada em segurança da informação, mais especificamente na área de wireless attack."],  "action": False},  {"UUID": 2, "Words": ["abra", "site", "url", "a", "o", "navegador", "na"], "Actions": {"url": "", "vetores": ["url", "site"]}, "type": "str", "payload": [], "response": ["Okay, abrindo!!"], "action": openUrl}, {"UUID": 3, "Words": ["abra", "youtube", "pesquisa","pesquise", "por", "navegador", "no"], "Actions": {"url": "", "vetores": ["pesquise", "por"]}, "type": "str", "payload": [], "response": ["Okay, estarei abrindo..", "Abrindo!", "Claros mestre!", "Pra ontem mestre!"], "action": openInYoutube}, 
     {"UUID": 4, "Words": ["quantos", "são", "sao", "é", "eh", "vezes", "*", "mais", "+", "menos", "-","dividido", "/", "porcento", "%", "?", "raiz", "calcule"], "Actions": {"url": "", "vetores": ["sao", "são", "eh", "é"]}, "type": "str", "payload": [], "response": [""], "action": Math},
     {"UUID": 5, "Words": ["o", "número", "numero", "é", "eh", "par", "par?"], "Actions": {"url": "", "vetores": ["numero", "número", "valor"]}, "type": "str", "payload": [], "response": [""], "action": parNumber}, {"UUID": 6, "Words": ["sorteie", "gere", "valor", "numero", "entre"], "Actions": {"url": "", "vetores": ["entre"]}, "type": "str", "payload": [], "response": [""], "action": generateRandomByStdin}]
    # {"UUID": 4, "Words": ["quantos", "são", "sao", "é", "eh", "vezes", "*", "mais", "+", "menos", "-","dividido", "/", "porcento", "%", "?"], "Actions": {"url": "", "vetores": []}, "type": "str", "payload": [], "response": [""], "action": Math}
