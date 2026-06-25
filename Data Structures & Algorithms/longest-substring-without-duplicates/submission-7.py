class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        res = 1
        curr_set = set()

        if s == "":
            return 0

        curr_set.add(s[i])

        while j < len(s):
            if s[j] in curr_set:
                curr_set.remove(s[i])
                i += 1
            else:
                res = max(res, j - i + 1)
                curr_set.add(s[j])
                j += 1
        return res
