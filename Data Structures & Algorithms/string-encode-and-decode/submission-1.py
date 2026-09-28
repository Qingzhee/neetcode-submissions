class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in strs:
            word = str(len(i)) + "#" + i + word     
        return word
    
    def decode(self, s: str) -> List[str]:
        arr = []
        while len(s)>0:
            j = s.index("#")                    
            counts = int(s[:j])    
            if counts == 0:
                arr.append("")
                s = s[j+1:]                    
                continue
            else:
                arr.append(s[j+1:j+1+counts])   
                s = s[j+1+counts:]
        return arr[::-1]