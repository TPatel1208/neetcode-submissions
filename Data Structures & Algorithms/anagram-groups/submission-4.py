class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = []
        indexes = {}
        index = 0
        for word in strs:
            key = tuple(sorted(word))
            if key in indexes:
                outputs[indexes[key]].append(word)
            else:
                indexes[key] = index
                outputs.append([])
                outputs[index].append(word)
                index+=1
        return outputs


