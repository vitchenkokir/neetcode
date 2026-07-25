class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for st in strs:
            res += str(len(st)) + '#' + st
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != '#':
                i += 1
            length = int(s[j:i]) + 1
            res.append(s[i+1:i+length])
            i += length
        return res

