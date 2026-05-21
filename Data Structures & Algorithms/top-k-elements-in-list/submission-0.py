class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for number in nums:
            count[number] = count.get(number, 0) + 1
        
        for i in range(k):
            max_key = max(count, key=count.get)
            output.append(max_key)
            del count[max_key]
        return output
