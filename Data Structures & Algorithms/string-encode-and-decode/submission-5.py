class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            delimiter = str(len(s)) + ":"
            encoded_str += delimiter + s
        
        return encoded_str 

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        i = 0
        colon_index = 0 
        while i < len(s):
            colon_index = s.find(':', i)
            number=""

            for c in s[i : colon_index]:
                number += c
            
            start = colon_index + 1

            # 3:yes
            end = colon_index + int(number) + 1
            decoded_list.append(s[ start : end ])
            i = end
        
        return decoded_list