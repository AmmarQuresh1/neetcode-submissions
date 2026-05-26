class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid//len(matrix[0])][mid%len(matrix[0])] > target:
                r = mid - 1
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] < target:
                l = mid + 1
            else:
                return True
        
        return False