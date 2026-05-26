class TimeMap:
    def __init__(self):
        self.timestamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timestamp[key]
        l, r = 0, len(values) - 1
        res = -1

        while l <= r:
            mid = (l+r)//2

            if values[mid][1] <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        if res == -1:
            return ""
        
        return values[res][0]

