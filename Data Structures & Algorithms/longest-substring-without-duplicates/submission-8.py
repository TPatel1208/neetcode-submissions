class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        p1 = 0
        p2 = 0
        curr = 0
        long = 0

        while p2 < len(s):
            if s[p2] not in chars:
                chars.add(s[p2])
                curr+=1
                long = max(curr,long)
                p2+=1

                
            else:
                while s[p2] in chars:
                    chars.discard(s[p1])
                    curr-=1
                    p1+=1
                
        return long