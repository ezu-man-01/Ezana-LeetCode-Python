class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for i in s:
            if i in '0123456789':
                string += i
            elif i.isalpha():
                string += i.lower()

        reversee = string[::-1]
        if reversee == string:
            return True
        else:
            return False