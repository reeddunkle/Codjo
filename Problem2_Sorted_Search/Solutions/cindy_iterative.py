def find(item, ordered_list):

    high_value = len(ordered_list)
    low_value = 0

    count = 0

    while(high_value >= low_value and count < len(ordered_list)//2):
        mid_value = (low_value + high_value)//2

        if item == ordered_list[mid_value]:
            return mid_value

        elif item > ordered_list[mid_value]:
            low_value = mid_value + 1

        else:
            high_value = mid_value - 1

        count += 1

    return -1
