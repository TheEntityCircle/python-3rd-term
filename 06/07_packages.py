"""
Теперь у нас есть пакет из нескольких файлов внутри
"""

# Явно импортируем разные компоненты, для демо сделаем это в разном виде
import simple_package.foo
from simple_package import bar

# Теперь можно всё-таки что-то выполнить
simple_package.foo.foo()
bar.bar()
