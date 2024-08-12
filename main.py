import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():

    url = "https://randomword.com/"
    translator = Translator()

    try:
        response = requests.get(url)
        #print(response.text)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        russian_word = translator.translate(english_words, dest="ru").text.strip()
        russian_definition = translator.translate(word_definition, dest="ru").text.strip()

        return {
            "russian_word" : russian_word,
            "russian_definition" : russian_definition
        }
    except:
        print("Ошибка")

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("russian_word")
        word_definition = word_dict.get("russian_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Ответ правильный!")
        else:
            print(f"Ответ не верный, было загадано слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()