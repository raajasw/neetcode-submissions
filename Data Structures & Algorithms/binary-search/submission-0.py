class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
            elif i == len(nums)-1 and nums[i] != target:
                return int(-1)
            
        
            
        