class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    
        word_map = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            word_map[tuple(count)].append(s)
        
        return list(word_map.values())
