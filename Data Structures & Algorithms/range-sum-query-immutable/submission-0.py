class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(self.nums)):
            self.prefix[i + 1] = self.prefix[i] + self.nums[i] 
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        res = self.prefix[right + 1] - self.prefix[left]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)