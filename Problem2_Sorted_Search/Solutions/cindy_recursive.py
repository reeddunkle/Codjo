def find(item, ordered_list):

    if ordered_list == []:
        return -1

    length = len(ordered_list)
    index_point = length//2
    number = ordered_list[index_point]

    if item == number:
        return index_point

    if length == 1:
        return -1

    if item < number:
        index_point = find(item, ordered_list[:index_point])
        return index_point

    if item > number:
        ip = index_point
        index_point = find(item, ordered_list[index_point:])
        if index_point != -1:
            index_point += ip
        return index_point
