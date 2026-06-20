class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
                
        for char in s:
            if char in t_map and t_map[char] >= 1:
                t_map[char] -= 1
            else:
                return False

        for (char, count) in t_map.items():
            if count != 0:
                return False
        
        return True
