class Solution:
    def isPalindrome(self, s: str) -> bool:

        def checkValid(ch):

            if (ch >= "0" and ch <= "9") or (ch >= "a" and ch <= "z"):
                return True

                return False

        st = ""
        for i in range(len(s)):
            ch = s[i]

            if checkValid(ch.lower()):
                st = st + s[i].lower()

        if st == st[::-1]:
            return True

        return False
