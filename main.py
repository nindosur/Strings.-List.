    # 1
value1 = input("Введите пример для вычисления: ")
print(value1, "=",eval(value1))

    # 2
import random
res = [random.randrange(-20, 20) for i in range(20)]
print("Рандомный список чисел: " + str(res))
a = max(res)
print("Максимальное число: ", a)
b = min(res)
print("Минимальное число: ", b)
i = 0
print('Сумма положительных чисел: ', sum(i > 0 for i in res))
print('Сумма отрицательных чисел: ', sum(i < 0 for i in res))
print('Сумма чисел равных нулю: ', sum(i == 0 for i in res))

