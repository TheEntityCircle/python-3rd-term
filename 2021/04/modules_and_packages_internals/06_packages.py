"""
Теперь у нас есть пакет из нескольких файлов внутри
"""

# Давайте импортируем всё, что в нём есть
from simple_package import *

# ... и попробуем как-нибудь достучаться до содержимого
simple_package.foo.foo()
simple_package.bar.bar()
foo.foo()
bar.bar()
foo()
bar()

"""
Попробуем это выполнить
"""
