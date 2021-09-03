from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0; higher = len(numbers) - 1
        while higher >= lower:
            temp = numbers[lower] + numbers[higher] 
            if temp == target:
                return [lower+1, higher+1]
            elif temp < target:
                lower += 1
            else:
                higher -= 1
        return [-1, -1]
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [i, hash_table[target - num]]
            else:
                hash_table[num] = i

test = [-1,0,1,0]
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSumHash([2,7,11,15], 9))