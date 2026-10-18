class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            length = len(s)
            prefix = str(length)+"%"
            strs[i] = prefix + s
        
        return "".join(strs)
                  

    def decode(self, s: str) -> List[str]:
        dec = []
        count = 0
        while count < len(s):
            sl = []
            while s[count]!='%':
                sl.append(s[count])
                count+=1
            length = int("".join(sl))
            dec.append(s[count+1:count+1+length])
            count = count + length +1
        return dec
        
            
            

