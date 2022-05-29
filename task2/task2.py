import operator
from enum import Enum

hex_def = "0x"
char_to_int = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
int_to_char = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}


class ENDIAN(Enum):
    BIG = 1
    LITTLE = 2


def find_and_delete_not_need(hex):
    if not operator.contains(hex, hex_def):
        return
    return hex.replace(hex_def, "")


def count_hex(only_bit_str):
    res = 0
    for index, char in enumerate(only_bit_str):
        if char.isdigit():
            value = int(char)
        else:
            char = char.lower()
            value = char_to_int.get(char)
        res += 16 ** index * value
    return res


def big_endian(inside):
    inside = find_and_delete_not_need(inside)[::-1]
    ans = count_hex(inside)
    return ans


def little_endian(inside):
    ans = count_hex(find_and_delete_not_need(inside))
    return ans


def show(value):
    print(f'VALUE {value}')
    print(f'Number of bytes: {len(find_and_delete_not_need(value)) / 2}')
    print(f'Little-endian: {little_endian(value)}')
    print(f'Big-endian: {big_endian(value)}')


def convert_to_hex(value):
    max_power = find_max(value)
    res = ''
    for i in range(max_power, -1, -1):
        data = find_multiply(value, i)
        value = value - (16 ** i * data)
        if data > 9:
            res_ = int_to_char[data]
        else:
            res_ = str(data)
        res += res_
    return res


def find_max(v):
    i = 1
    while 16 ** i <= v:
        i += 1
    return i - 1


def find_multiply(v, power):
    multiply = 1
    while (16 ** power) * multiply <= v:
        multiply += 1
    return multiply - 1


def from_endian_to_hex(val, endian):
    res = convert_to_hex(val)
    if endian == ENDIAN.BIG:
        res = res[::-1]
    return hex_def + res


if __name__ == '__main__':
    show("0xff00000000000000000000000000000000000000000000000000000000000000")
    print("---")
    show("0xaaaa000000000000000000000000000000000000000000000000000000000000")
    print("---")

    show("0xFFFFFFFF")
    print("---")

    show(
        "0xF000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    print("----")
    print(from_endian_to_hex(100, ENDIAN.BIG))
    print(from_endian_to_hex(100, ENDIAN.LITTLE))
