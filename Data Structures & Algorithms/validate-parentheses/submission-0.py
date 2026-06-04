class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opent = ('(','[','{')
        close = (')', '}', ']')
        for char in s:
            if char in opent:
                stack.append(char)
            else:
                if stack and char in close:
                    if (stack[-1] == '(' and char == ')') \
                    or (stack[-1] == '{' and char == '}') \
                    or (stack[-1] == '[' and char == ']'):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if not stack else False