class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i, j in zip(word1, word2):
            merged.append(i + j)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)

