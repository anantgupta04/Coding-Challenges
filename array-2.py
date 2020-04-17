'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def division(input_list):
    prod = 1
    for i in input_list:
        prod *= int(i)
    output = [prod // i for i in input_list]
    print('Resultant array = ', output)
    return output


def division_less(lst):
    l = len(lst)
    left_list = [1] * (l + 1)
    right_list = [1] * (l + 1)
    output = [1] * l
    for i in range(1, l + 1):
        left_list[i] = left_list[i - 1] * lst[i - 1]
    print('left_list = ', left_list)
    for i in range(l - 1, -1, -1):
        right_list[i] = right_list[i + 1] * lst[i]
    print('right_list = ', right_list)
    for i in range(1, l + 1):
        output[i - 1] = left_list[i - 1] * right_list[i]
    print(output)


if __name__ == '__main__':
    n = [int(i) for i in input('Enter numbers separated by space: ').split(' ')]
    result = division(n)
    result_2 = division_less([2, 3, 2, 5])
