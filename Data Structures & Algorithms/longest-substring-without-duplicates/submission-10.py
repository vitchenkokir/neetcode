class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        st = set()
        while r < len(s):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            res = max(res, len(st))
            r += 1
        return res