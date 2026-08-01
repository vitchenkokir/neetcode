class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
                 ')':'(',
                 ']':'[',
                 '}':'{'
                 }
        stack = []
        for st in s:
            if st not in pairs:
                stack.append(st)
            else:
                if not stack or stack[-1] != pairs[st]:
                    return False
                stack.pop()
        return not stack