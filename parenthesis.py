'''
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
'''


class Solution:
    def isValid(self, s):
        flag = False
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        para = []
        i = 0
        while (not flag and i < len(s)):
            if s[i] in open_brackets:
                para.append(s[i])
            elif s[i] in close_brackets:
                pos = close_brackets.index(s[i])
                bracket = para.pop(-1)
                flag = False if bracket == open_brackets[pos] else True
            i += 1
        print('Para at end of FOR loop = ', para)
        return (len(para) == 0)


if __name__ == '__main__':
    s = '((()))'  # Test case 1 VALID
    s = '({[)]'  # Test case 2 INVALID
    # s = '[()]{}' #Test case 3 VALID
    obj = Solution()
    print(obj.isValid(s))
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    # print(map)
