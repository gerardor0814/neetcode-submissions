class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapping.keys():
            self.mapping[key].append([value, timestamp])
        else:
            self.mapping[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping.keys():
            return ""
        else:
            l = 0
            r = len(self.mapping[key]) - 1
            retval = ""
            while l < r:
                mid = int((l+r) / 2)
                if self.mapping[key][mid][1] <= timestamp:
                    retval = self.mapping[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            if self.mapping[key][l][1] <= timestamp:
                return self.mapping[key][l][0]
            else:
                return retval