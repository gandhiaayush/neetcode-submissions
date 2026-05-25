import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = float("inf")


        while left <= right:
            mid = (left + right) // 2
            total_time = 0 

            total_time = sum(math.ceil(p / mid) for p in piles)
            
            if total_time <= h:
                min_speed = min(min_speed, int(mid))
                right = mid - 1
            
            else:
                left = mid + 1

        return min_speed
        







        