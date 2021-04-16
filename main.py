import functools
import time

from random import randint


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args):
        start_time = time.monotonic()
        result = func(*args)
        print(f'{func.__name__}: {time.monotonic() - start_time} seconds')
        return result
    return wrapper


@timeit
def built_sorted(unsorted_array: list):
    return sorted(unsorted_array)


@timeit
def built_sort(unsorted_array: list):
    temp_array = unsorted_array.copy()
    temp_array.sort()
    return temp_array


@timeit
def bubble_sort(unsorted_array: list):
    temp_array = unsorted_array.copy()
    max_item = len(temp_array)
    while max_item > 1:
        for item_pos in range(0, max_item-1):
            item = temp_array[item_pos]
            if item_pos != max_item and item > temp_array[item_pos+1]:
                    temp_array[item_pos], temp_array[item_pos+1] = temp_array[item_pos+1], item
            if item_pos + 1 == max_item - 1:
                max_item -= 1
    return temp_array


if __name__ == '__main__':
    array = []
    while len(array) < 100:
        rand_item = randint(0, 100)
        if rand_item not in array:
            array.append(rand_item)

    print(array)
    print(bubble_sort(array))
    print(built_sorted(array))
    print(built_sort(array))
    print(array)

