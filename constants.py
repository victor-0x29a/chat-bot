from config.actions import enable_airmon

INDECISIVE_MESSAGES = [
    "Ops! Você pode repetir de forma clara?",
    "Talvez eu precise ter mais informações.",
    "Desculpe, não entendi a pergunta.",
    "Você poderia reformular a pergunta?",
    "Pode repetir a pergunta?",
    "Não estou entendendo o que você está dizendo.",
    "Você poderia ser mais específico?",
    "Poderia ser mais claro, por favor?",
    "Desculpe, não estou entendendo.",
    "Por favor, explique a questão novamente."
]
ERROR_MESSAGES = ["Hum, houve um erro, tente novamente mais tarde!"]
LEARNING_LEVEL = 3

ACTIONS = [
    {
        "UUID": 0,
        "Words": [
            "ative", "o",
            "modo", "airmon",
            "airmon-ng",
            "rede", "inicie"
        ],
        "Actions": {"vetores": [""]},
        "type": "str",
        "response": [],
        "action": enable_airmon
    }
]
