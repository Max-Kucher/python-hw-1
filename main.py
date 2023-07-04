def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль."
    else:
        return a / b


def calculator():
    print("Добро пожаловать в программу Калькулятор!\n")

    while True:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление\n")

        operation = input("Введите ваш выбор (1-4): ")

        if operation == '1':
            result = add(num1, num2)
            print("\nРезультат сложения: ", result)
        elif operation == '2':
            result = subtract(num1, num2)
            print("\nРезультат вычитания: ", result)
        elif operation == '3':
            result = multiply(num1, num2)
            print("\nРезультат умножения: ", result)
        elif operation == '4':
            result = divide(num1, num2)
            print("\nРезультат деления: ", result)
        else:
            print("\nНеверный ввод.")

        repeat = input("\nХотите продолжить? (Y/N): ")
        if repeat.lower() != 'y':
            print("\nЗавершаем выполнение программы")
            break


calculator()
