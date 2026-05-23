class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers) - 1
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            low = 0 
            high = length

            while low <= high:
                mid = (high + low) // 2
                
                if numbers[mid] == new_target and mid != i:
                    return [i + 1, mid + 1]
                
                elif numbers[mid] >= new_target:
                    high = mid - 1
                
                else:
                    low = mid + 1



        