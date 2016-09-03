def flip_it(num):
    binary_num = ~num & 0b11111111111111111111111111111111
    return binary_num
