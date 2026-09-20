class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = []
        columns = []
        for i in range(0 , len(matrix)):
            rows.append(matrix[i])
        

        for j in rows:
            if target in j:
                return True
        

        return False

        