with open('first.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Введите данные:')
        file.write(f'{line}\n')
        if not line:
            exit('Данные внесенны в файл first.txt')
