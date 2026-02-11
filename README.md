# 3Sum Smaller

## 🧩 Problem Statement

Given an array of `n` integers `nums` and an integer `target`, return the **number of index triplets** `(i, j, k)` such that:

- `0 <= i < j < k < n`
- `nums[i] + nums[j] + nums[k] < target`

The goal is to count all valid triplets that satisfy the condition.
(Source: https://thita.ai/problems/sum-smaller)

---

## 📝 Example

### Example 1

**Input:**
nums = [-2, 0, 1, 3]
target = 2


**Output:**
2


**Explanation:**

The valid triplets are:

- `(-2, 0, 1)` → sum = -1 < 2  
- `(-2, 0, 3)` → sum = 1 < 2  

So the result is `2`.

---

## 🚀 Approach

1. Initialize a counter `ans` to store the number of valid triplets.
2. Fix the first index `i` from `0` to `n - 3`.
3. Fix the second index `j` from `i + 1` to `n - 2`.
4. Fix the third index `k` from `j + 1` to `n - 1`.
5. For each triplet `(i, j, k)`:
   - Check if:
     ```
     nums[i] + nums[j] + nums[k] < target
     ```
   - If true, increment `ans`.
6. Return the final count.

---

## ⏱️ Time and Space Complexity

**Time Complexity:**
- Sorting: `O(n log n)`
- Two-pointer traversal: `O(n²)`
- Overall: `O(n²)`

**Space Complexity:**
- `O(1)` (if sorting in place)

---

## 🧠 Key Concepts

- Sorting
- Two-pointer technique
- Efficient counting strategy
- Avoiding brute force `O(n³)`

---

## 📌 Edge Cases

- `nums.length < 3` → return `0`
- All numbers are negative
- All numbers are positive
- Duplicate values
- Very large or very small `target`

---

## 🎯 Summary

This problem is a variation of the classic **3Sum** problem.  
Instead of returning triplets, we count how many triplets satisfy a condition.

The optimal solution uses sorting and a two-pointer approach to reduce the time complexity from `O(n³)` to `O(n²)`.

Solution for this problem is based on code from following link: https://www.geeksforgeeks.org/dsa/count-triplets-with-sum-smaller-than-a-given-value/

---

⭐ Feel free to star this repository if you found it helpful!
