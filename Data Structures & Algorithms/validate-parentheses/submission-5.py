class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their opening pairs
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen: # If it's a closing bracket
                # Check if stack is not empty and top matches the required opening bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else: # If it's an opening bracket
                stack.append(char)
                
        return len(stack) == 0
            
        