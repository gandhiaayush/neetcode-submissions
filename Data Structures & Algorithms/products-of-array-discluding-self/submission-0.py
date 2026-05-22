class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = math.prod(nums)
        if product != 0:
            for i in range(len(nums)):
                output.append(int(product / nums[i]))
            return output
        else:
            for i in range(len(nums)):
                temp_var = nums[:i] + nums[i+1:]
                output.append(math.prod(temp_var))
            return output