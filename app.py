from config.limits import speak, getPhrase
from config.data import listActions
from constants import INDECISIVE_MESSAGES


class out:
    def __init__(self, stdin):
        self.itensOrganizados = [] # uuid - total [1, 1 ,1, 1,1,1]
        self.choices = []
        self.std = stdin.lower().split()
        self.stdin = stdin
        for acao in listActions():
            for palavras in acao["Words"]:
                for palavra in self.std:
                    if (palavra == palavras):
                        self.choices.append(acao["UUID"])

    def error(self):
        return ["Hum, houve um erro, tente novamente mais tarde!"]
    def MinAprendizado(self):
        return 3
    def coletaPorVetor(self, frase, vetor, type, initials):
        # frase para percorrer
        # vetor para buscar os dados depois do vetor
        # tipo de dados que ele esta buscando apos o vetor
        self.stringToArray = frase.split()
        if type == "str":
            self.word = "'"
            self.vector = ""
            self.foundSearch = False
            for letter in frase:
                if self.foundSearch:
                    self.vector += letter
                if letter == " " and not self.foundSearch:
                    for palavra in initials:
                        if palavra == self.word:
                            self.word = ""
                            self.foundSearch = True
                    if not self.foundSearch:
                        self.word = ""
                elif letter != " " and not self.foundSearch:
                    self.word += letter
            return self.vector
        for word in self.stringToArray:
                if word == vetor:
                    self.stringToArray.remove(word)
                    break
                else:
                    self.stringToArray.remove(word)
        self.newArray = []
        for item in self.stringToArray:
            self.obj = item.replace(",", "")
            if type == "int":
                self.inteiros = [1,2,3,4,5,6,7,8,9]
                for i in self.inteiros:
                    if self.obj == str(i):
                        self.newArray.append(self.obj)

        return self.newArray
    def start(self):
        for item in self.choices:
            self.found = False
            for obj in self.itensOrganizados:
                if (obj["UUID"] == item):
                    self.found = True
                    obj["total"].append(1)
            if not self.found:
                self.itensOrganizados.append({"UUID": item, "total": [1]})

        self.top = {"UUID": 0, "total": 0} # Here this vector of action to execute
        for item in self.itensOrganizados:
            self.total = 0
            for i in item["total"]:
                self.total+=1
            if self.total > self.top["total"]:
                self.top = {"UUID": item["UUID"],"total": self.total}

        if (self.top["total"] < self.MinAprendizado()):
            return speak(getPhrase(INDECISIVE_MESSAGES))
        for item in listActions():
            if item["UUID"] == self.top["UUID"]:
                if not item["Actions"]["vetores"]:
                    speak(getPhrase(item["response"]))
                if item["action"]:
                    item["action"]()
                    return
                for palavra in item["Actions"]["vetores"]:
                    if palavra in self.stdin:
                        self.dados = self.coletaPorVetor(self.stdin, palavra, item["type"], item["Actions"]["vetores"])
                        if self.dados and item["action"]:
                            speak(getPhrase(item["response"]))
                            item["action"](self.dados)
                        else:
                            speak(self.error())


while True:
    stdin = str(input("-> "))
    IA = out(stdin)
    IA.start()
