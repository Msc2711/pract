import random


def solve_case_3() -> None:
    numbers: list[int] = []

    print("Программа генерирует случайные числа.")
    print("Введите 0 для остановки.\n")

    while True:
        random_number: int = random.randint(1, 100)

        print(f"Сгенерировано число: {random_number}")

        user_input: int = int(input("Введите 0 для остановки или любое другое число для продолжения: "))

        if user_input == 0:
            break

        numbers.append(random_number)

    print(f"\n{'=' * 40}")
    print(f"Всего сгенерировано чисел (с учётом последнего): {len(numbers) + 1}")
    print(f"Чисел, выводимых на экран (кроме последнего): {len(numbers)}")

    if len(numbers) == 0:
        print("\nПользователь остановил программу сразу (введён 0).")
        print("Нет чисел для вывода.")
    else:
        print(f"\nСписок чисел (кроме последнего): {numbers}")


if __name__ == "__main__":
    solve_case_3()
