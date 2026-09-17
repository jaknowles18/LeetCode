class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counts = defaultdict(int)
        index = -1

        for char in s:
            counts[char] += 1

        count = 0
        for char in s:
            if counts.get(char) == 1:
                return count
            
            count += 1
        
        return index
