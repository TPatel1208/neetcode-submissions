class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        avail = self.timemap[key]
        low = 0
        high = len(avail)
        while low < high:
            mid = (high-low)//2+low
            if avail[mid][0] == timestamp:
                return avail[mid][1]
            elif avail[mid][0] < timestamp:
                low = mid+1
            else:
                high = mid

        if low == 0:
            return ""
        return avail[low-1][1]
        

