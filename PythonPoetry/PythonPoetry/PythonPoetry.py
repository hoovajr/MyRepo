import os

f = open("Python Poem.txt")
text = f.read()

# lower() not really needed since no uppercase, but practicing my methods :)
#char_list = [x for x in text if x.lower() >='a' and x.lower() <= 'z']

letter_count_dict = {}

for letter in text:
    if letter >= 'a' and letter <= 'z':
        if letter in letter_count_dict.keys():
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1

print(letter_count_dict)