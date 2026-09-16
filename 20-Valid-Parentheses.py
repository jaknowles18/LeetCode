class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in s:

            if i == "(":
                stack.append(")")
                continue

            if i == "[":
                stack.append("]")
                continue

            if i == "{":
                stack.append("}")
                continue

            if len(stack) == 0:
                return False

            if stack.pop() != i:
                return False
            
        if len(stack) == 0:
            return True
        
        return False
            
            
