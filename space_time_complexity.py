'''
Asked by: Stripe
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def check(arr):
    result = 1
    min = 2147483648
    for i in range(0, len(arr)):
        print('element = ', arr[i])
        if arr[i] < min:
            min = arr[i]
            result = min + 1
            print('Inside FOR--min result = ', min)
        elif arr[i] == result:
            result += 1
    return result


if __name__ == '__main__':
    arr = [int(i) if int(i) > 0 else 0 for i in input('Enter numbers separated by space: ').split(' ')]
    print(arr)
    # arr = [1, 2, 0]
    print('minimum result = ', check(arr))
