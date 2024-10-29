from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # Corrected to len(nums) for proper index
        
        while left < right:  # Loop until the pointers converge
            mid = (left + right) // 2  # Use integer division for index
            if nums[mid] < target:
                left = mid + 1  # Move left pointer
            else:
                right = mid  # Move right pointer
            
        return left  # Return the insertion index
