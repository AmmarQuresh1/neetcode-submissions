class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + ":" + s
        return encode

    def decode(self, s: str) -> List[str]:
        res = []
        s_end = 0
        while True:
            if s_end == len(s):
                return res
            delimiter = int(s[s_end:s.find(":", s_end)])
            s_start = s.find(":", s_end)
            s_end = s_start + delimiter + 1
            res.append(s[s_start+1:s_end])

