class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            curr_set = set()
            curr_set.add(s[i])
            curr_length = 1
            
            for j in range(i + 1, len(s)):
                if s[j] in curr_set:
                    break
                
                curr_set.add(s[j])
                curr_length += 1
            
            res = max(res, curr_length)
        return res