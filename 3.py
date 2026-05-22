def find_antonym():
    """
    Функция находит антоним заданного слова
    """

    antonyms = {}

    N = int(input())

    for i in range(N):
        pair = input()
        word1, word2 = pair.split()
        antonyms[word1] = word2
        antonyms[word2] = word1

    search_word = input()

    if search_word in antonyms:
        print(antonyms[search_word])
    else:
        print(search_word)


find_antonym()