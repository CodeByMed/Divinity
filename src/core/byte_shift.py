'''
def left_shift(data, shift_amount):
    return data << shift_amount

def right_shift(data, shift_amount):
    return data >> shift_amount

def circular_left_shift(data, shift_amount, bit_size=32):
    return ((data << shift_amount) | (data >> (bit_size - shift_amount))) & ((1 << bit_size) - 1)

def circular_right_shift(data, shift_amount, bit_size=32):
    return ((data >> shift_amount) | (data << (bit_size - shift_amount))) & ((1 << bit_size) - 1)
'''