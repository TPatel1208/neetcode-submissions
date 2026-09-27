class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        buckets = [[] for i in range(len(nums)+1)]
        for key, freq in freq_map.items():
                buckets[freq].append(key)
        result = []
        pointer = len(buckets)-1
        i=0
        while(i<k):
            for num in buckets[pointer]:
                result.append(num)
                i+=1
            pointer-=1
        return result
