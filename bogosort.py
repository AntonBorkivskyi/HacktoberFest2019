# Python program for implementation of BogoSort 
# This code is provided by Bohdan Borkivskyi

import random


def sort(list):
    goal = sorted(list)
    while list != goal:
        print(list)
        random.shuffle(list)
    return list


if __name__ == '__main__':
    print(sort([2, 1, 3]))
