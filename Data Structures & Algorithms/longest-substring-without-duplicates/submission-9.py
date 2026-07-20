class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        st = set()
        l, r = 0, 0
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            r += 1
            res = max(res, len(st))
        return res