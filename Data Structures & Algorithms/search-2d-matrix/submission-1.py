class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1 
        for element in matrix:
            if target > element[0]:
                row += 1
                continue
            elif target == element[0]:
                return True
            break
        
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] > target:
                right = mid - 1
                continue
            
            left = mid + 1
        return False
            

        