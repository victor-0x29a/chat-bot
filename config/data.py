# ID REFERENTE - PALAVRAS QUE VAI PROCURAR NA PERGUNTA - VETORES PARA BUSCAR DADOS DEPOIS
from .limits import speak, getPhrase
from config.actions import enableAirmon

def listActions():
        return [{"UUID": 0, "Words": ["ative", "o", "modo", "airmon", "airmon-ng", "rede", "inicie"], "Actions": { "vetores": [""]}, "type": "str", "response": [],  "action": enableAirmon},]
    # {"UUID": 4, "Words": ["quantos", "são", "sao", "é", "eh", "vezes", "*", "mais", "+", "menos", "-","dividido", "/", "porcento", "%", "?"], "Actions": {"url": "", "vetores": []}, "type": "str", "payload": [], "response": [""], "action": Math}

    
    # Se nao houver itens no campo ["vetores"], ele apenas fala! 
