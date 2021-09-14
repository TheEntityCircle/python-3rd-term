"""
Работа с глобальными переменными в Python несколько специфична.
"""

# Пусть у нас есть глобальная переменная.
# Это всегда так себе идея. Но пусть есть.
TEST = 1

# Эта функция хочет читать глобальную переменную - имеет право.
def func1():
    print("Inside func1", TEST)

# Эта функция хочет писать в глобальную переменную.
# И как будто ей дали это сделать. Но нет.
def func2():
    TEST = 10
    print("Inside func2", TEST)

# А вот эта функция правда сможет писать в глобальную переменную.
def func3():
    global TEST
    TEST = 10
    print("Inside func3", TEST)


print("Initial value", TEST)
func1()

print("Before func2 call", TEST)
func2()
print("After func2 call", TEST)

print("Before func3 call", TEST)
func3()
print("After func3 call", TEST)