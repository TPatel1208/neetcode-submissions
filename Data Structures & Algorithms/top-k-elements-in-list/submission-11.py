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
        
        top_knums = []
        topk=0
        for item in reversed(buckets):
            for num in item:
                top_knums.append(num)
                topk+=1
                if(topk==k):
                    return top_knums
