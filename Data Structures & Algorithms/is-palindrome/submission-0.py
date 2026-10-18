class Solution:
    def isPalindrome(self, s: str) -> bool:
        beg = 0
        end = len(s)-1
        while beg<end:
            if not s[beg].isalnum():
                beg+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            if(s[beg].lower() != s[end].lower()):
                return False
            beg+=1
            end-=1
        return True
    