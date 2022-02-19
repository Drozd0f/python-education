def read_with_try(file: str) -> str:
    f = open(file, 'r')
    try:
        text = f.read()
    finally:
        f.close()
    return text


def context_manager_read(file: str) -> str:
    with open(file, 'r') as f:
        text = f.read()
    return text


def write_with_try(file: str):
    f = open(file, 'a')
    try:
        f.write('new line\n')
    finally:
        f.close()


def context_manager_write(file: str):
    with open(file, 'a') as f:
        f.write('new line\n')


if __name__ == '__main__':
    write_with_try('text.txt')
    print(read_with_try('text.txt'))
    context_manager_write('text.txt')
    print(context_manager_read('text.txt'))

