import collections

class TimeMap:

    def __init__(self):
        self.timemap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        values = self.timemap[key]

        left, right = 0, len(values) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] > timestamp:
                right = mid - 1
            
            elif values[mid][1] < timestamp:
                result = values[mid][0]
                left = mid + 1

            else:
                return values[mid][0]
        return result 
            




        
