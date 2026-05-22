def translate_phrase():
    """
    Функция переводит фразу с русского на английский язык.
    """

    dictionary = {}

    N = int(input())

    for i in range(N):
        pair = input()
        russian_word, english_word = pair.split()
        dictionary[russian_word] = english_word

    phrase = input()
    words = phrase.split()

    result_words = []
    for word in words:
        if word in dictionary:
            result_words.append(dictionary[word])
        else:
            result_words.append(word)

    print(" ".join(result_words))


translate_phrase()
