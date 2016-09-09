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
riddle = ''

for i in [56, 38, 44, 56, 29]:
    for key, value in letter_count_dict.items():
        if value == i:
            riddle += key

print(riddle)

for key, value in letter_count_dict.items():
    print(key, value)

# Write a program that generates all such riddles based on this poem.

words_list = []
words_list  = [line.rstrip('\n') for line in open('Words.txt')]

# riddle_list is a list of lists - each individual list is a riddle
riddle_list = []
riddle_solution_list = []

for word in words_list:
    temp_riddle = []
    for i in range(0, len(word)):
        letter = word[i]        
        if letter in letter_count_dict.keys():
            temp_riddle.append(letter_count_dict[letter])
            if i == len(word) - 1:
                riddle_list.append(temp_riddle)
                riddle_solution_list.append(word)
        else:
            break

print(riddle_list)
print(len(riddle_list))
print(riddle_solution_list)

# What is the longest word that is a solution to a riddle based on this poem? (useful: Words (Unix))
largest_riddle_list = []
length_largest_riddle = 0

for i in riddle_list:
    if len(i) > length_largest_riddle:
        largest_riddle_list = []
        largest_riddle_list.append(i)
        length_largest_riddle = len(i)
    elif len(i) == length_largest_riddle:
        largest_riddle_list.append(i)
    else:
        continue

print("The length of the largest riddle is ", length_largest_riddle)
print("The number of riddles this length is ", len(largest_riddle_list))
print("The riddles with the largest length are:")
for i in largest_riddle_list:
    print(i)


