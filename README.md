# Longest Increasing Path in a Matrix

**Difficulty:** Hard  
**Tags:** Dynamic Programming, DFS, Memoization  

---

## 🧩 Problem
Given an m x n integers matrix, return the length of the longest increasing path.  
You can move in four directions: left, right, up, or down.  
You may NOT move diagonally or move outside of the boundary.

**Example:**
Input: [[9,9,4],[6,6,8],[2,1,1]] Output: 4 Explanation: The longest increasing path is [1, 2, 6, 9]






---

## 🧠 Approach
We use **DFS + Memoization**:
- Start DFS from every cell.
- Store longest path length for each cell in a memo table (`dp`).
- Explore 4 directions only if the next cell has a higher value.
- Avoid redundant recalculations by caching results.

---

## ⏱️ Complexity
- **Time:** O(m × n)
- **Space:** O(m × n)

---

## 🧑‍💻 Code
See `solution.py` for the full implementation.
