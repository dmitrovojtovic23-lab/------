# Завдання 1
def get_odd_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i
# Завдання 2
def get_outside_range(data_list, start, end):
    for item in data_list:
        if item < start or item > end:
            yield item
# Завдання 3
def horizontal_line(symbol):
    print(symbol * 20)
def vertical_line(symbol):
    for i in range(5):
        print(symbol)
def show_line(symbol, function_to_call):
    function_to_call(symbol)
# Завдання 4 та 5
def simple_decorator(func):
    def wrapper(start, end):
        print("Початок обчислення...")
        result = func(start, end)
        print("Обчислення завершено!")
        return result
    return wrapper
@simple_decorator
def get_even_numbers(start, end):
    evens = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(list(get_odd_numbers(1, 10)))
show_line("*", horizontal_line)
print(get_even_numbers(0, 100000))