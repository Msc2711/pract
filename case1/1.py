def solve_case_1() -> None:
    n: int = int(input("Введите размер массива N: "))

    A: list[float] = []
    print(f"Введите {n} элементов массива:")
    for i in range(n):
        element: float = float(input(f"A[{i}] = "))
        A.append(element)

    sum_positive: float = 0.0
    count_positive: int = 0

    for element in A:
        if element > 0:
            sum_positive += element
            count_positive += 1

    print("\nРезультаты:")
    print(f"Массив: {A}")
    print(f"Количество положительных элементов: {count_positive}")
    print(f"Сумма положительных элементов: {sum_positive}")


if __name__ == "__main__":
    solve_case_1()
