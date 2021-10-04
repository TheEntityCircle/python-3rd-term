"""
Изнанка декораторов, часть 3.
А здесь всё то же самое, но чуть объёмнее:
- оборачиваемой функции передаются все параметры (при том, что их состав неизвестен);
- обёртка передаёт возвращаемое значение вызвавшему;
- декоратор пытается изобразить какую-то полезную деятельность.
"""

import time


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def do_smth():
    time.sleep(0.1)
    return 42


res = do_smth()
print(res)