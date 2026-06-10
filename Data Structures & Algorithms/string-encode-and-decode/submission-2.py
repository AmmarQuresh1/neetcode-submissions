class Solution:

    def encode(self, strs: List[str]) -> str:
        # Insert length prefix for each string 
        encodeStr = ""
        for s in strs:
            # example "4:neet"
            encodeStr += str(len(s)) + ":" + s
        return encodeStr
    def decode(self, s: str) -> List[str]:
        # Use length prefix to split strings
        decodeList = []
        index = 0
        prefixIndex = 0
        while index < len(s):
            prefix = ord(f"{s[index]}") - ord("0")
            if s[index] == ":":
                prefix = ord(f"{s[prefixIndex:index]}")
                decodeList.append(s[index+1:index+1+prefix])
                index += prefix + 1
                prefixIndex = index
            if index == len(s):
                break

        return decodeList

        
                


