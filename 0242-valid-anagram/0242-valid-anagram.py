class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = "".join(sorted(s)) 
        y = "".join(sorted(t))

        if x == y and len(s) == len(t):
            return True

        return False
