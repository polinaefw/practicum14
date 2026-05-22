def count_descendants():
    """
    Функция строит генеалогическое дерево и рекурсивно считает количество потомков
    """

    family_tree = {}

    N = int(input())

    for i in range(N):
        parent, child = input().split()
        if parent not in family_tree:
            family_tree[parent] = []
        family_tree[parent].append(child)

    search_name = input()

    def dfs(name):
        """
        Внутренняя рекурсивная функция для подсчета потомков
        """
        if name not in family_tree:
            return 0

        total = 0
        for child in family_tree[name]:
            total += 1
            total += dfs(child)
        return total

    print(dfs(search_name))

count_descendants()