
with open('fifth.txt', 'w', encoding='utf-8') as file:

    file.write(user_numbers)

with open('fifth.txt', 'r', encoding='utf-8') as file:

    for number in file:
        print(sum(map(float, number.split())))
