class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map:
                continue
            else:
                num_map[nums[i]] = i
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res in num_map and num_map[res] != i:
                return [min(i, num_map[res]), max(i, num_map[res])]
