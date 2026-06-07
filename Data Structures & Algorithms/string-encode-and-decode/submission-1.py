class Solution:

    def encode(self, strs: List[str]) -> str:
        Res = ""
        for s in strs:
            Res += str(len(s)) + "#" + s
        return Res


            

    def decode(self, s: str) -> List[str]:
        my_list, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            my_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return my_list
        

        
