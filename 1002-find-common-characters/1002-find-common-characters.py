class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        output = Counter(words[0])

        for word in words[1:]:
           output = output & Counter(word)

        return list(output.elements())

