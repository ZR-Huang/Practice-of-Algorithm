'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Note:
- Division between two integers should truncate toward zero.
- The given RPN expression is always valid. That means the expression would 
    always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem.isdigit() or elem[1:].isdigit(): # if elem is negative number, isdigit() will return false
                stack.append(int(elem))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if elem == "+":
                    tmp = first_num + second_num
                elif elem == "-":
                    tmp = first_num - second_num
                elif elem == "*":
                    tmp = first_num * second_num
                else:
                    sign = -1 if first_num * second_num < 0 else 1
                    tmp = abs(first_num) // abs(second_num)
                    tmp *= sign
                stack.append(tmp)
        return stack[0]
                
print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
