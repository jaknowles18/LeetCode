# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        upper = n
        lower = 0
        mid = (upper + lower) // 2

        if (upper == 0):
            return 0

        while (isBadVersion(mid) != True or isBadVersion(mid - 1) != False):
            mid = (upper + lower) // 2

            if (upper < lower):
                return 0

            if (isBadVersion(mid)):
                upper = mid - 1
            
            if (isBadVersion(mid) == False):
                lower = mid + 1

            
        return mid

