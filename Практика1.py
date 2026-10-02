# задача 1
tempurature_C = 20
Farengete = (tempurature_C * 9/5) + 32
Kelvin = tempurature_C + 273.15
print(f"Kelnin: {Kelvin}")
print(f"Farengete: {Farengete}")

#  задача 2
n = int(input("Введите число:"))
if n // 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
if n > 0:
    print("Положительное")
elif n < 0:
    print("Отрицательное")
else:
    print("Ноль")
if 10 <= n <= 50:
    print('Да')
else:
    print("Нет")

# задача 3
import random

spec = "!@#$%^&*"
let = "QWERTYUIOPASDFGHJKLZXCVBNM"
count1 = 3
count2 = 2

dice = random.randint(1, 10)
dice2 = random.randint(1, 10)
letter = random.choices(let, k=count1)
special = random.choices(spec, k=count2)
password = f"{dice}{dice2}{''.join(letter)}{''.join(special)}"

print(password)


# задача 4
from collections import Counter
text = input().lower()
counts = Counter(text)

for symbol, count in counts.items():
    print(symbol)
    print(count)

# задача 5

N = int(input())

numbers = [True] * (N + 1)

numbers[0] = False
numbers[1] = False

for i in range(2, N + 1):
    if numbers[i]:
        for j in range(i * 2, N + 1, i):
            numbers[j] = False

for i in range(2, N + 1):
    if numbers[i]:
        print(i, end=" ")
