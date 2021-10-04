"""
Нюансы областей видимости
"""

# Есть некоторая переменная 
a = 5

# Эта функция просто её печатает
def report_value():
    print("The value is:", a)

# А эта функция печатает и меняет
def do_some_work():
    # ... явно сказав, что намерена работать с глобальной переменной
    global a
    print("Current value:", a)
    a += 1
    print("New value:", a)


# Попробуем это всё выполнить
report_value()
do_some_work()
report_value()
