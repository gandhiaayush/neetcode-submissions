class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:      # left half [left..mid] is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1          # target in sorted left half
                else:
                    left = mid + 1           # target in rotated right half

            else:                            # right half [mid..right] is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1           # target in sorted right half
                else:
                    right = mid - 1          # target in rotated left half

        return -1