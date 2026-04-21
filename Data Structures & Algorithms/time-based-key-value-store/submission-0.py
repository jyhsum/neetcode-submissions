class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([value, timestamp])
        else:
            self.data[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        res, values = "", self.data[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
