class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        
        for num in nums:

            if num != 0:
                nums[count] = num
                count += 1
                continue
            
        
        
        for count in range(count, len(nums)):
            nums[count] = 0
            


        