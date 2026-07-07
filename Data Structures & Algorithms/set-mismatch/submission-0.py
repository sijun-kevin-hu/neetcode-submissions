class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_set = {}
        for num in nums:
            if num in num_set:
                num_set[num] += 1
            else:
                num_set[num] = 1

        res = [0] * 2
        for i in range(1, len(nums) + 1):
            print(i)
            if i not in num_set:
                res[1] = i
            else:
                if num_set[i] == 2:
                    res[0] = i
        return res