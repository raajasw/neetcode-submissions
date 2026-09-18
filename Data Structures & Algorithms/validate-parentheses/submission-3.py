class Solution:
    def isValid(self, s: str) -> bool:
        list_a = []
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                list_a.append(s[i])
            elif s[i] == ')' and list_a and list_a[-1] == '(':
                list_a.pop()
            elif s[i] == ']' and list_a and list_a[-1]  == '[':            list_a.pop()
            elif s[i] == '}' and list_a and list_a[-1]  == '{':
                list_a.pop()
            else:
                return False

        return False if list_a else True
            
        