"""This module contains binary search for exersice Algorithms - practice"""


def binary_search(array: list, number_search: int) -> int:
    """This function return index search number"""
    if array != sorted(array):
        raise ValueError(f'{array} don\'t sorted list')
    start = 0
    end = len(array)
    while start <= end:
        center = (start + end) // 2
        if number_search == array[center]:
            return center
        if number_search < array[center]:
            end = center - 1
        else:
            start = center + 1
