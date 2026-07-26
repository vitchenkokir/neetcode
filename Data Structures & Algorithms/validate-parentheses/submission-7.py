class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        for st in s:
            if st not in pairs:
                stack.append(st)
            else:
                if not stack or pairs[st] != stack[-1]:
                    return False
                stack.pop(-1)
        return not stack