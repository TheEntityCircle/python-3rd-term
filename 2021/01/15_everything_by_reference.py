"""
В C++ было много нюансов с передачей параметров в функции.
Можно было передавать по значению, по указателю, по ссылке. И ещё были const-ы.
Как это устроено в Python-е? Несколько иначе.
Бывают неизменяемые типы данных (immutable) и изменяемые (mutable).
Всё immutable передаётся по значению. Всё mutable - по ссылке.
"""


def change_list(l):
    l.append(42)
    l[0] = -1


def change_string(s):
    s += " test"
    print("Inside function: %s" % s)


my_list = [1, 2, 3]
print(my_list)
change_list(my_list)
print(my_list)


my_string = "string"
print(my_string)
change_string(my_string)
print(my_string)


"""
Строго говоря, всё передаётся "по присваиванию" (by assignment).
То есть вообще-то всё всегда передаётся по ссылке, а сама ссылка - по значению.
Далее immutable сущности не могут быть изменены вообще никак.
А mutable могут быть изменены (потому что ссылка), но не могут быть переприсвоены (потому что ссылка по значению).
Но вспоминать об этих тонкостях стоит только тогда, когда хотите странного (или уже его сотворили и отлаживаете).
"""