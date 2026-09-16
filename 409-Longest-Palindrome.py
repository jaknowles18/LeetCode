class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = len(s)

        count = Counter(s)
        even_count = 0
        multi_odd = 0
        off_by_one = 0

        for val in count:
            if (count.get(val) % 2 == 0):
                even_count = even_count + count.get(val)

            if (count.get(val) % 2 != 0 and count.get(val) > 1):
                multi_odd = multi_odd + count.get(val) - 1
                off_by_one = 1
            if (count.get(val) == 1):
                off_by_one = 1
        
        if (length % 2 == 0):
            return even_count + multi_odd + off_by_one

        return even_count + multi_odd + off_by_one