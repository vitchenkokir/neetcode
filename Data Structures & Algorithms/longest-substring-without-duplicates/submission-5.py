class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        st = set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            max_len = max(max_len, len(st))
        return max_len