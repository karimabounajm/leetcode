from typing import List


class Solution:
    def threeSumSorted(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        answer = []
        for i in range(length):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                lower = i + 1
                higher = length - 1
                while higher > lower:
                    temp = nums[i] + nums[lower] + nums[higher]
                    if temp == 0:
                        answer.append([nums[i], nums[lower], nums[higher]])
                        lower += 1
                        higher -= 1
                        while lower < higher and nums[lower] == nums[lower-1]:
                            lower += 1
                    elif temp < 0:
                        lower += 1
                    else:
                        higher -= 1
        return answer

    def threeSumHash(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        answer = []
        for i in range(length):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                lower = i + 1
                higher = length - 1
                while higher > lower:
                    temp = nums[i] + nums[lower] + nums[higher]
                    if temp == 0:
                        answer.append([nums[i], nums[lower], nums[higher]])
                        lower += 1
                        higher -= 1
                        while lower < higher and nums[lower] == nums[lower-1]:
                            lower += 1
                    elif temp < 0:
                        lower += 1
                    else:
                        higher -= 1
        return answer


test = [1, 1, 1, 1]
sol = Solution()
print(sol.threeSumSorted(test))
print(sol.threeSumHash(test))
