class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip()
        array = x.split(" ")
        return len(array[-1])
    
        