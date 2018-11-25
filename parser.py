# -*- coding: utf-8 -*-

def count_glasn(word):
    glasn = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я',
             'Ю', 'Ё', 'Е']
    i = 0
    for b in glasn:
        i += word.count(b)
    return i


def count_soglas(word):
    soglas = ["й", "ц", "к", "н", "г", "ш", "щ", "з", "х", "ф", "в", "п", "р", "л", "д", "ж", "ч", "с", "м",
              "т", "б", "Й", "Ц", "К", "Н", "Г", "Ш", "Щ", "З", "Х", "Ф", "В", "П", "Р", "Л", "Д",
              "Ж", "Ч", "С", "М", "Т", "Б"]
    r = 0
    for n in soglas:
        r += word.count(n)
    return r

def count_punct(word):
    punct = [",", ".", "!", ";", ":", "?"]
    j = 0
    for s in punct:
        j += word.count(s)
    return j

def count_words(word):
    word = word.split()
    return len(word)



if __name__ == "__main__":
    file = input('Введите имя файла:')
    try:
        input_file = open(file, 'r', encoding='utf-8')
        sog = 0
        glas = 0
        point = 0
        word1 = 0
        for line in input_file:
            sog += count_soglas(line)
            glas += count_glasn(line)
            point += count_punct(line)
            word1 += count_words(line)
        print("Согласных букв:",sog)
        print("Гласных букв:", glas )
        print("Количество знаков припенания в тексте:", point)
        print("Количество слов в тексте:", word1)
    except FileNotFoundError:
        print(file, "не найден")

