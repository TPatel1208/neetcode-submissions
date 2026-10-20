class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums)-1
        while beg<=end:
            mid = (end-beg)//2+beg
            if nums[mid]==target:
                return mid
            if nums[mid] >= nums[beg]:
                if nums[beg] <= target < nums[mid]:
                    end = mid-1
                else:
                    beg = mid+1
            else:
                if nums[mid] < target <= nums[end]:
                    beg = mid +1
                else:
                    end = mid-1
        return -1
