class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = len(numbers)-1
        p2 = 0

        while numbers[p1] + numbers[p2] != target:
            if numbers[p1] + numbers[p2] >= target:
                p1 -=1 
            else:
                p2+=1
        
        return [p2+1,p1+1]
