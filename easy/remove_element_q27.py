class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        for i in range(len(nums)):
            if val == nums[i]:
                a += 1
                i += 1
        return len(nums) - a