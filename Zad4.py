#Zad4

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania funkcji {func.__name__}: {end_time - start_time: .4f} sekund.")
        return result

    return wrapper

@timeit
def example_function():
    time.sleep(1)

example_function()

