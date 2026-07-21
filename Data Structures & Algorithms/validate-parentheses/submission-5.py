class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []
        for st in s:
            if st not in pairs:
                stack.append(st)
            else:
                if not stack or pairs[st] != stack[-1]:
                    return False
                stack.pop()
        return not stack