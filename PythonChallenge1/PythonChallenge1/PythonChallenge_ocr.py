f = open('rare_chars.txt')
my_string = f.read()

char_dict = {}

for char in my_string:
    if char in char_dict.keys():
        char_dict[char] += 1
    else:
        char_dict[char] = 1

print(char_dict)