def add_elements():
    A = list(map(int, input("Введіть список чисел: ").split()))

    left = int(input("Елемент на початок: "))
    right = int(input("Елемент у кінець: "))

    A.insert(0, left)
    A.append(right)

    print(A)

    return A

add_elements()