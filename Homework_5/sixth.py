import re


def numbers(nums):
    return sum([int(i) for i in nums])


my_dict = {}

with open('sixth.txt', 'r', encoding='utf-8') as file:
    for line in file:
        subject, *lessons = line.split()
        lessons = ' '.join(lessons)
        nums = re.findall(r'\d+', lessons)
        my_dict[subject.split(':')[0]] = numbers(nums)
    print(my_dict)
