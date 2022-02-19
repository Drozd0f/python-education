numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers_words = [1, 2, 3, 'hello', 'world']

second_name = names[1]

for i in numbers_words:
    if isinstance(i, (int, float)):
        numbers.append(i)
    elif isinstance(i, str):
        strings.append(i)


if __name__ == '__main__':
    print(numbers)
    print(strings)
    print(f'The second name on the names list is {second_name}')
