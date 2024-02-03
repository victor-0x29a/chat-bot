from .chatbot import ChatBot

while True:
    stdin = str(input("-> "))
    CHAT = ChatBot(stdin)
