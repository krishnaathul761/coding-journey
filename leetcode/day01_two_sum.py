# ===================================
# LeetCode #1 - Two Sum
# Difficulty: Easy
# Date: February 2026
# ===================================

# PROBLEM:
# Given array nums and target,
# return indices of two numbers that add up to target

# EXAMPLE:
# Input:  nums = [2,7,11,15], target = 9
# Output: [0,1]
# Because 2 + 7 = 9

# SOLUTION:
class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Dictionary: stores {number: position}
        
        for i, num in enumerate(nums):
            complement = target - num  # Number we need to find
            
            if complement in seen:  # Found the pair!
                return [seen[complement], i]
            
            seen[num] = i  # Remember this number

# WHAT I LEARNED:
# - Dictionary (seen = {}) stores key:value pairs
# - enumerate() gives index AND value while looping
# - complement = the number we're looking for
# - This approach is O(n) - checks each number once
