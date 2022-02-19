mystring = 'hello'
myfloat = 10.1
myint = 20


if __name__ == '__main__':
    if mystring == 'hello':
        print(f'String: {mystring}')
    if isinstance(myfloat, float) and myfloat == 10.0:
        print(f'myfloat is float and equal {myfloat}')
    if isinstance(myint, int) and myint == 20:
        print(f'myint is int and equal {myint}')
