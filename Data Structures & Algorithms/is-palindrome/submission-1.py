class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for st in s:
            new_st = st.lower()
            if new_st.isalnum():
                word += new_st
        return word == word[::-1]