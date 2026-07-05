class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        looked = {}
        max_freq = 0
        best_length = 0

        i, j = 0, 0
        while j < len(s):
            if s[j] in looked:
                    looked[s[j]] += 1
            else:
                looked[s[j]] = 1
            max_freq = max(max_freq, looked[s[j]])

            if (j - i + 1) - max_freq > k:
                looked[s[i]] -= 1
                i += 1
            else:
                best_length = max(best_length, j - i + 1)
            j += 1
        return best_length


