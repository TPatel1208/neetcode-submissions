class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0;
        current_length = 0;
        current = 0;
        second = 0;
        substring = {}
        while second < len(s):
            if s[second] in substring:
                if current_length > max_length:
                    max_length = current_length
                while s[second] in substring:
                    substring.pop(s[current])
                    current +=1
                    current_length-=1
            else:
                substring[s[second]] = s[second]
                current_length+=1
                second+=1
        
        return max(current_length,max_length)
