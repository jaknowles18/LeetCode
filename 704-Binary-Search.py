class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        len1 = len(nums)
        lower = 0 
        upper = len1 - 1
        
        if len1 == 0:
            return -1

        while (upper >= lower):
            half = (lower + upper)// 2
            curr = nums[half]

            if (curr == target):
                return half

            if (curr < target):  
                lower = half + 1
        
            if (curr > target):
                upper = half - 1

        return -1
        