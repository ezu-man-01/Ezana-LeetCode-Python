class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = []
        for i in range(len(digits)):
            digit.append(str(digits[i]))
        
        joined = "".join(digit)
         
        plus = int(joined) + 1

        string_plus = str(plus)
        finall = []

        for i in range(len(string_plus)):
            finall.append(int(string_plus[i]))
        
        return finall

