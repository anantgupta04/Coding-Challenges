'''
his problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

Bonus: solution in O(n) time?
'''


def staircase_recursion(n):
    ans = 0
    # print('Value of n = ', n)
    if (n == 0) or (n == 1):
        return 1
    else:
        prev_2 = staircase_recursion(n - 2)
        prev_1 = staircase_recursion(n - 1)
        ans = prev_2 + prev_1
    return ans


def staircase_nonrecursion(n):
    ans = [0 for _ in range(n + 1)]
    ans[0] = 1
    ans[1] = 1
    if n > 2:
        for i in range(2, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2]
    return ans[n]


if __name__ == '__main__':
    # print('Non recursion 5 = ',staircase_nonrecursion(5))
    # print('recursion 4= ',staircase_recursion(4))  # 5
    # print('recursion 5 = ',staircase_recursion(5))  # 8
    # print('recursion 35 = ',staircase_recursion(35))
    print('Non recursion = ', staircase_nonrecursion(35))
