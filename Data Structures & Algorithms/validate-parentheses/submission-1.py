class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            
            elif i == ')':
                if len(stack) == 0:
                    return False

                last = stack.pop()
                if last != '(':
                    return False
            
            elif i == ']':
                if len(stack) == 0:
                    return False

                last = stack.pop()
                if last != '[':
                    return False
            
            elif i == '}':
                if len(stack) == 0:
                    return False

                last = stack.pop()
                if last != '{':
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False