# Longest Increasing Path in a Matrix
# Difficulty: Hard
# Tags: Dynamic Programming, DFS, Memoization

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        Given an m x n integers matrix, return the length of the longest increasing path.
        You can move in four directions: left, right, up, or down.
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # Memoization table
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j):
            # Return cached result if already computed
            if dp[i][j]:
                return dp[i][j]
            
            max_len = 1  # Each cell alone counts as length 1
            
            # Explore all 4 possible directions
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(x, y))
            
            dp[i][j] = max_len
            return dp[i][j]
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result


# Example usage
if __name__ == "__main__":
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    solution = Solution()
    print(solution.longestIncreasingPath(matrix))  # Output: 4
