"""This module contains quick sort for exersice Algorithms - practice"""


def _refactor_array(array: list, pivot: int) -> list:
    """This function return new array after rearranging the numbers"""
    left = list(filter(lambda number: number < pivot, array))
    center = list(filter(lambda number: number == pivot, array))
    right = list(filter(lambda number: number > pivot, array))
    return left + center + right


def quick_sort(array: list) -> list:
    """This function return array after sorted"""
    pivot = array[0]
    array = _refactor_array(array, pivot)
    last_pivots = [pivot]
    idx = 0
    while idx != len(array):
        pivot = array[idx]
        if pivot not in last_pivots:
            array = _refactor_array(array, pivot)
            last_pivots.append(pivot)
        else:
            idx += 1
    return array
