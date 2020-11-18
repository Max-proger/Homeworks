rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
numbers = []
with open('fourth.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1)
        numbers.append(rus[i[0]] + ' ' + i[1])

with open('fourth_2.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(numbers)
