class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        s_set = set()
        i, j = 0, 1

        if s == "":
            return 0

        s_set.add(s[i])


        while j < len(s):
            if s[j] in s_set:
                s_set.remove(s[i])
                i += 1
            else:
                s_set.add(s[j])
                curr_len = j - i + 1
                res = max(res, curr_len)
                j += 1
        return res