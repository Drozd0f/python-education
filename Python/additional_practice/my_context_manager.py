"""This module contains the implementation context manager for working with files"""
import logging


class MyContextManager:
    """This class describes context manager for working with files"""
    def __init__(self, file: str, method: chr, encoding: str = 'utf-8'):
        self._file = open(file, method, encoding=encoding)  # pylint: disable=R1732
        # (consider-using-with)

    def __enter__(self):
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logging.info(f'Exception {exc_val} has been handled')
        self._file.close()
        return True


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )
    with MyContextManager('some_file.txt', 'a') as f:
        f.write('some text\n')

    with MyContextManager('some_file.txt', 'r') as f:
        print(f.read())

    with MyContextManager('some_file.txt', 'r') as f:
        f.abc()

    with MyContextManager('some_file.txt', 'r') as f:
        print(f.read())
