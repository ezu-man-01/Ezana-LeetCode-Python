class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(heights)):
            min_high = i
            for j in range(i + 1 ,len(heights)):
                if heights[min_high] > heights[j]:
                    min_high = j
                
            heights[i], heights[min_high] = heights[min_high], heights[i]
            names[i], names[min_high] = names[min_high], names[i]
        
        names.reverse()
        return names