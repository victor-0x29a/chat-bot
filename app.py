from constants import (
    INDECISIVE_MESSAGES,
    ERROR_MESSAGES,
    LEARNING_LEVEL,
    ACTIONS
)
from config.actions import speak, get_phrase


class ChatBot:
    def __init__(self, stdin):
        self.organized_items = []
        self.choices = []
        self.std = stdin.lower().split()
        self.stdin = stdin
        for action in ACTIONS:
            for action_word in action["Words"]:
                for std_word in self.std:
                    if (std_word == action_word):
                        self.choices.append(action["UUID"])

        self.call()

    def collect_by_vector(self, phrase, vector, type, initials):
        words_from_phrase = phrase.split()
        if type == "str":
            word = "'"
            vector = ""
            is_found = False

            for letter in phrase:
                if is_found:
                    vector += letter
                if letter == " " and not is_found:
                    for palavra in initials:
                        if palavra == word:
                            word = ""
                            is_found = True
                    if not is_found:
                        word = ""
                elif letter != " " and not is_found:
                    word += letter

            return vector

        for word in words_from_phrase:
            if word == vector:
                words_from_phrase.remove(word)
                break
            else:
                words_from_phrase.remove(word)

        new_list = []
        int_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for item in words_from_phrase:
            if type != "int":
                return

            obj = item.replace(",", "")

            for int_number in int_array:
                if obj == str(int_number):
                    new_list.append(obj)

        return new_list

    def call(self):
        for item in self.choices:
            is_item_found = False

            for obj in self.organized_items:
                if (obj["UUID"] == item):
                    is_item_found = True
                    obj["total"].append(1)

            if not is_item_found:
                self.organized_items.append({"UUID": item, "total": [1]})

        top = {"UUID": 0, "total": 0}

        for item in self.organized_items:
            total = 0
            for i in item["total"]:
                total += 1
            if total > top["total"]:
                top = {"UUID": item["UUID"], "total": total}

        if (top["total"] < LEARNING_LEVEL):
            return speak(get_phrase(INDECISIVE_MESSAGES))

        for action in ACTIONS:
            if action["UUID"] == top["UUID"]:
                vectors = action["Actions"]["vectores"]

                if not vectors:
                    speak(get_phrase(action["response"]))

                if action["action"]:
                    return action["action"]()

                for vector_word in vectors:
                    if vector_word in self.stdin:
                        data = self.collect_by_vector(
                            self.stdin,
                            vector_word,
                            action["type"],
                            vectors
                        )
                        if data and action["action"]:
                            speak(get_phrase(action["response"]))
                            action["action"](data)
                        else:
                            speak(ERROR_MESSAGES)


while True:
    stdin = str(input("-> "))
    CHAT = ChatBot(stdin)
