
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.BIT = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.initialize(i+1, nums[i])
    def initialize(self, i: int, value: int) -> None:
        while i <= len(self.nums):
            self.BIT[i] += value
            i += i & -i    
    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        self.initialize(i+1, diff)
    def sumRange(self, left: int, right: int) -> int:
        return self.helperSum(right+1) - self.helperSum(left)
    def helperSum(self, i: int) -> int:
        acumi = 0
        while i > 0:
            acumi += self.BIT[i]
            i -= i & -i
        return acumi
    def scale(self, val: int) -> None:
        for i in range(len(self.nums)):
            self.nums /= val
            self.BIT /= val