class Solution:
    def maxArea(self, heights: List[int]) -> int:
        end = len(heights) -1
        beg = 0
        curr = min(heights[beg], heights[end]) * (end-beg)
        while beg<end:
            if heights[beg] > heights[end]:
                end-=1
            else:
                beg+=1
            curr = max(curr, min(heights[beg], heights[end]) * (end-beg))

        return curr
                