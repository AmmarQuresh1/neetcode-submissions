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
        while True:
            prefix = ord(f"{index}") - ord("0")
            if prefix < 10 and s[index+1] == ":":
                decodeList.append(s[index+1:index+1+prefix])
                index += 1 + prefix
            else:
                return decodeList

        
                


