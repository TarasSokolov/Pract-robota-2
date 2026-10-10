def squares():
    n = int(input("Кількість елементів: "))

    A = set()

    for i in range(1, n + 1):
        if i * i <= 1000:
            A.add(i * i)

    print(*sorted(A))

    return A

squares()