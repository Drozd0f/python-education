"""This module contains the implementation decorator with runtime logging"""
import logging
import time


def my_decor(func):
    """This function describes implementation decorator with runtime logging"""
    def wrapped(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        logging.info(f'Time execution = {time.time() - start}')
    return wrapped


@my_decor
def some_func():
    """This function describes subtracting a number to test the decorator"""
    number = 1000
    while number > 0:
        number -= 7


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)s - %(levelname)s - %(message)s'
    )
    some_func()
