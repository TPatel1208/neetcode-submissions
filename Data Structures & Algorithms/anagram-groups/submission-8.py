class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexes = {}
        for word in strs:
            letters = [0]*26
            for char in word:
                letters[ord(char) - ord('a')]+=1
            key = tuple(letters)
            if key in indexes:
                indexes[key].append(word)
            else:
                indexes[key] = [word]
        return list(indexes.values())


