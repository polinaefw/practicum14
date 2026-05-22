def sort_words(text):
    '''
    Выводит слова в порядке уменьшения их частоты в строке
    '''
    words = text.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for word in sorted_words:
        print(word)


input_text = input()

sort_words(input_text)
