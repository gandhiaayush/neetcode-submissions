class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberset = set(nums)
        longest = 0 
        for element in nums:
            if (element - 1) not in numberset:
                length = 0 
                while (element + length) in numberset:
                    length += 1
                longest = max(length, longest)
        return longest

