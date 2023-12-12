class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect_right(self.meta[key], timestamp)
        if i == 0:
            return ''
        return self.data[key][i - 1]