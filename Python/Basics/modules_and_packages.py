import re


if __name__ == '__main__':
    find_members = [some_func for some_func in dir(re) if 'find' in some_func]
    print(find_members)
