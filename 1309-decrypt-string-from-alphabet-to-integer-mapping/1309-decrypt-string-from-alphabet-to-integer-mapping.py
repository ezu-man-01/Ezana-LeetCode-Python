class Solution:
    def freqAlphabets(self, s: str) -> str:
        p = ""
        skip = 0
        for i in range(len(s)-1 , -1, -1):
            if skip != 0:
                skip -=1
                continue
            
            if s[i] != '#':
                change = int(s[i])
                if 1 <= change <= 9:
                    x = chr(ord('a')+ change -1)
                    p = str(x) + p
                
            if s[i] == '#':
                num = int(s[i - 2:i])
                p = chr(ord('a') + num - 1) + p
                skip = 2
            
        return p




            