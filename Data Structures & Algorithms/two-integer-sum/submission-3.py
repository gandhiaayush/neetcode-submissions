class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_target = 0
        for index in range(len(nums)):
            new_target = target - nums[index]
            for new in nums:
                if new == new_target and nums.index(new_target) != index:
                    idx = nums.index(new_target)
                    return sorted([index, idx])