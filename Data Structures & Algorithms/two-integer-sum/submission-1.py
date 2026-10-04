class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in matches:
                return [matches[needed],index]
            matches[num] = index
    #time complexity O(n)
    #space complexity O(n)