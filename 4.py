def find_item_form():
    """
    Функция определяет форму предмета
    """

    items_dict = {}

    N = int(input())

    for i in range(N):
        line = input()
        words = line.split()

        form = words[0]

        items = words[1:]

        for item in items:
            items_dict[item] = form

    search_item = input()

    if search_item in items_dict:
        print(items_dict[search_item])
    else:
        print(search_item)


find_item_form()