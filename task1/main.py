import random
from datetime import datetime

list_of_keys_size = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
list_with_generated = []


def task1():
    for number in list_of_keys_size:
        print(two_in_power(number))


def task2():
    for item in list_with_generated:
        print(item)


def ""():
    for i in range(len(list_with_generated)):
        print(f'start brute force data for  {list_of_keys_size[i]} bytes')
        time_start = datetime.now()
        brute_force(two_in_power(list_of_keys_size[i]), list_with_generated[i])
        taken_time = datetime.now() - time_start
        print(f'its takes {taken_time}')
        print("--------------------------")


def two_in_power(power_value):
    return 2 ** power_value


def generate_rnd_list():
    for number in list_of_keys_size:
        list_with_generated.append(random_hex_value_under_then(number))


def random_hex_value_under_then(max_value):
    return hex(random.randint(0, two_in_power(max_value)))


def brute_force(max_value, data):
    for i in range(max_value):
        if data == i:
            return


if __name__ == '__main__':
    generate_rnd_list()
    print('task1 ')
    task1()
    print("------------------")
    print("task2")
    task2()
    print("-------------------")
    print("task3")
    task3()
