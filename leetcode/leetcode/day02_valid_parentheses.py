# ===================================
# LeetCode #20 - Valid Parentheses
# Difficulty: Easy
# Date: February 2026
# ===================================

# PROBLEM:
# Given string with brackets: ( ) [ ] { }
# Check if they're valid (properly closed)

# EXAMPLES:
# "()"     → Valid ✅
# "()[]{}" → Valid ✅
# "(]"     → Invalid ❌
# "([)]"   → Invalid ❌

# SOLUTION:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stack to track opening brackets
        
        # Dictionary: closing bracket → opening bracket
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for char in s:
            if char in pairs:  # Closing bracket?
                # Check if stack empty or top doesn't match
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()  # Remove matching opening bracket
            else:  # Opening bracket
                stack.append(char)  # Add to stack
        
        return len(stack) == 0  # Valid if stack empty

# WHAT I LEARNED:
# - Stack data structure (Last In, First Out)
# - Dictionary to map closing → opening brackets
# - stack.append() adds to top, stack.pop() removes from top
# - stack[-1] gets top element without removing
# - Matching brackets = valid opening/closing order
