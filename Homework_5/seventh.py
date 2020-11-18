import json
text = 'C:/Users/Home/Desktop/GeekBrains/Python/Урок 5. Работа с файлами/homework/seventh.txt'
text_2 = 'C:/Users/Home/Desktop/GeekBrains/Python/Урок 5. Работа с файлами/homework/seventhj.json'

with open(text, 'r', encoding='utf-8') as file:
    my_list = []
    my_dict = {}
    profit = 0
    i = 0
    ap = {}
    for line in file:
        name, form, proceeds, costs = line.split()
        my_dict[name] = float(proceeds) - float(costs)
        if my_dict.setdefault(name) > 0:
            profit += my_dict.setdefault(name)
            i += 1
    ap.update({'average profit': round(profit / i, 2)})
    my_list.append(my_dict)
    my_list.append(ap)

with open(text_2, 'w', encoding='utf-8') as file:
    json.dump(my_list, file)
