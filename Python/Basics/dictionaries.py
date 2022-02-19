phonebook = {
    'John': 938477566,
    'Jack': 938377264,
    'Jill': 947662781
}

phonebook.update({'Jake': 938273443})
phonebook.pop('Jill')

if __name__ == "__main__":
    if 'Jake' in phonebook:
        print('Jake is listed in the phonebook')

    if 'Jill' not in phonebook:
        print('Jill is not listed in the phonebook')
