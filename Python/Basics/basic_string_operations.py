s = "Str therae! wha ome!"

print(f"Length of s = {len(s)}")

print(f'The first occurrence of the letter a = {s.index("a")}')

print(f'a occurs {s.count("a")} times')


print(f'The first five characters are {s[:5]}')
print(f'The next five characters are {s[5:10]}')
print(f'The thirteenth character is {s[12]}')
print(f'The characters with odd index are {s[1::2]}')
print(f'The last five characters are {s[-5:]}')


print(f'String in uppercase: {s.upper()}')

print(f'String in lowercase: {s.lower()}')

if s.startswith('Str'):
    print('String starts with "Str". Good!')


if s.endswith('ome!'):
    print('String ends with "ome!". Good!')


print(f'Split the words of the string: {s.split()}')
