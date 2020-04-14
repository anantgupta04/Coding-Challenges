'''
Asked by facebook
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
'''


def singleNumber(nums):
    result = set()
    for i in nums:
        if i not in result:
            result.add(i)
        else:
            result.remove(i)
    return result.pop()


def approach_2():
    # Python3 code to find duplicates in O(n) time from Geek for Greeks
    # numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
    numRay = [-4, 3, 2, -4, 1, 1, 3, 2]
    arr_size = len(numRay);
    for i in range(arr_size):
        numRay[numRay[i] % arr_size] = numRay[numRay[i] % arr_size] + arr_size;
    print('Array = ', numRay)
    print("The non-repeating number is  : ");
    for i in range(arr_size):
        if (numRay[i] >= arr_size * 2):
            print(i, " ")
            # This code is contributed by 29AjayKumar


def constant_memory(num):
    sum = 0
    for i in num:
        sum = sum + i if (sum - i) <= 0 else sum - i
    print('Non-repeating number is =', sum)


if __name__ == '__main__':
    # print(singleNumber([4, 3, 2, 4, 1,1, 3, 2]))
    # approach_2()
    constant_memory([4, 3, 2, 4, 1, 3, 2])
