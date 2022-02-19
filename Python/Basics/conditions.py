number = 10
second_number = 10
first_array = []
second_array = [1, 2, 3]

number += 6
first_array.append(number)
temp_number = second_array.pop()
first_array.extend([second_number, temp_number])
first_array[0] = 1
second_number -= second_number

if __name__ == '__main__':
    if number > 15:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")

    if not second_number:
        print("6")
