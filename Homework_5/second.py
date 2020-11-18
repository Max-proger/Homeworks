from typing import TextIO

original_list: list[str] = ['Winter first', 'Spring second', 'Summer third', 'Autumn last']

with open('second.txt', 'w', encoding='utf-8') as file:
    file.writelines('%s\n' % line for line in original_list)

file: TextIO
with open('second.txt', 'r', encoding='utf-8') as file:
    words: int = 0
    lines: int = 0
    for line in file:
        lines += 1
        words += len(line.split())

    print(f'Количество строк равно: {lines}\nКоличество слов равно: {words}')
