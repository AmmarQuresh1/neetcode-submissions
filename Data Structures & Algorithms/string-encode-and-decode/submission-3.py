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
            if index == len(s):
                break
            
            colon = s.find(':', index)
            prefix = int(s[prefixIndex:colon])
            decodeList.append(s[colon+1:colon+1+prefix])
            index = colon + 1 + prefix
            prefixIndex = index

        return decodeList