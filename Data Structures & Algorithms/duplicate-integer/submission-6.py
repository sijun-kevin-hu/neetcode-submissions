class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        
        for (num, count) in nums_map.items():
            if count > 1:
                return True

        return False