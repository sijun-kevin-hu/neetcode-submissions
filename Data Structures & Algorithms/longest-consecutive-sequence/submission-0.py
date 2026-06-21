class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        for num in nums:
            longest_curr = 1
            num_plus = num + 1
            while num_plus in num_set:
                longest_curr += 1
                num_plus += 1
            longest = max(longest, longest_curr)
        return longest
        