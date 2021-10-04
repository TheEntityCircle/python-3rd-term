"""
Изнанка декораторов, часть 2.
Здесь происходит всё ровно то же самое.
Только синтаксис прикручивания обёртки теперь "декораторный".
"""

def test_decorator(func):
    def wrapper():
        print("Before the call")
        func()
        print("After the call")
    return wrapper


@test_decorator
def hello():
    print("Hello")


hello()