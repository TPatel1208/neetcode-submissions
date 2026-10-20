class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) -1

        while beg <= end:
            mid = (end-beg)//2 + beg
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid -1 
            else:
                beg = mid+1  
        
        return -1 