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
            colon = s.find(':', index)
            length = int(s[index:colon])
            start = colon + 1
            end = start + length
            decodeList.append(s[start:end])
            index = end

        return decodeList