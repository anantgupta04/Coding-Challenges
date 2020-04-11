'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def check(input_list, prod):
    output = [prod // i for i in input_list]
    print(output)
    return output


if __name__ == '__main__':
    prod = 1
    n = []
    for i in input('Enter numbers separated by space: ').split(' '):
        n.append(int(i))
        prod *= int(i)
    print((n), '\t', prod)
    result = check(n, prod)
