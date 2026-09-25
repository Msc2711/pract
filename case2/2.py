def solve_case_2() -> None:
    n: int = int(input("Введите размер массива N: "))
    B: float = float(input("Введите число B: "))

    A: list[float] = []
    print(f"Введите {n} элементов массива:")
    for i in range(n):
        element: float = float(input(f"A[{i}] = "))
        A.append(element)

    count_greater: int = 0
    product: float = 1.0

    for element in A:
        if element > B:
            product *= element
            count_greater += 1

    if count_greater == 0:
        product = 0.0

    print("\nРезультаты:")
    print(f"Массив: {A}")
    print(f"Число B: {B}")
    print(f"Количество элементов > B: {count_greater}")
    print(f"Произведение этих элементов: {product}")


if __name__ == "__main__":
    solve_case_2()
