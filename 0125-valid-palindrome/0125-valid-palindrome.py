class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i]
        return a==a[::-1]

        