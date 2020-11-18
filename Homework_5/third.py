from typing import TextIO, Any

f: TextIO
with open('third.txt', 'r', encoding='utf-8') as f:
    zp: list[Any] = []
    for line in f:
        worker, salary = line.split()
        zp.append(salary)
        if 20000 > float(salary):
            print(f'{worker}: зарплата меньше 20 000')
    print(f'Средняя величина дохода сотрудников равна: {sum(map(float, zp)) / len(zp)}')
