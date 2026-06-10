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
        while index < len(s):
            prefix = ord(f"{s[index]}") - ord("0")
            if prefix < 10 and s[index+1] == ":":
                decodeList.append(s[index+2:index+2+prefix])
                index += prefix + 2
            else:
                break

        return decodeList

        
                


