import math

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выйти")
    
    operation = input("Введите номер операции")
    if operation == '11':
        print("Выход из программы")
        break
    while True: 
        try: 
            x = int(input("Введите номер операции: ")) 
            break
        except ValueError: 
            print("Попробуйте снова")

    a = float(input("Введите число: "))

    if operation == 1:
        b = float(input("Введите второе число: "))
        print("Результат:", a + b) 
    elif operation == 2:
        b = float(input("Введите второе число: "))
        print("Результат:", a - b) 
    elif operation == 3:
        b = float(input("Введите второе число: "))
        print("Результат:", a * b) 
    elif operation == 4:
        b = float(input("Введите второе число: "))
        if b == 0:
            print("Ошибка: Делить на ноль нельзя") 
        else:
            print("Результат:", a/b) 
    elif operation == 5:
        b = float(input("Введите степень: "))
        print("Результат:", a ** b) 
    elif operation == 6:
        if a < 0:
           print("Ошибка: Квадратный корень из отрицательного числа")
        else: 
            print("Результат:", math.sqrt(a)) 
    elif operation == 7:
        if a < 0:
           print("Ошибка: Нет факториала отрицательного числа")
        else:
            factorial = 1
            for i in range(1, int(a)+1):
                factorial *= i
            print("Результат:", factorial)
    elif operation == 8:
        print("Результат:", math.sin(a))
    elif operation == 9:
        print("Результат:", math.cos(a))
    elif operation == 10:
        print("Результат:", math.tan(a))    
    else:
        print("Ошибка: Неправильный выбор операции")  