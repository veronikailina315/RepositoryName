# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, splitter=','):
    participants_a = set(participants_first_group.split(splitter))
    participants_b = set(participants_second_group.split(splitter))
    intersection_list = list(participants_a.intersection(participants_b))
    intersection_list.sort()
    return (intersection_list)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, splitter='|')
print (result)
# TODO Провеьте работу функции с разделителем отличным от запятой


