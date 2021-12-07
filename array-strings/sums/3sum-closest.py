from typing import List
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        if len(nums) == 3 or ans >= target:
            return ans
        for i in range(len(nums) - 2):
            num_i = nums[i]
            if i > 0 and nums[i - 1] == num_i:
                continue
            max_sum = num_i + nums[-1] + nums[-2]
            if max_sum < target:
                if abs(max_sum - target) < abs(ans - target):
                    ans = max_sum
                continue
            min_sum = num_i + nums[i + 1] + nums[i + 2]
            if min_sum > target:
                return min_sum if abs(target - min_sum) < abs(target - ans) else ans
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = num_i + nums[left] + nums[right]
                if three_sum == target:
                    return target
                if abs(three_sum - target) < abs(ans - target):
                    ans = three_sum
                if three_sum < target:
                    left += 1
                    while left < len(nums) - 1 and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while right > i and nums[right] == nums[right + 1]:
                        right -= 1
        return ans

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         # sorting the array to optimize searching
#         nums.sort()
#         # setting the arbitrarly close answer to the target as the
#         # sum of the first three elements
#         ans = nums[0] + nums[1] + nums[2]
#         # checking base case for input, in case of easy return, with 
#         # the second conditional checking if the sum of the 3 least 
#         # elements is greater than the target, meaning that all further
#         # combinations will be further away from the target
#         if len(nums) == 3 or ans >= target:
#             return ans
#         # outer loop, with i holding the index to the leftmost element
#         # in consideration
#         for i in range(len(nums) - 2):
#             num_i = nums[i]
#             if i > 0 and nums[i - 1] == num_i:
#                 continue
#             # checking base case, which is if the maximum sum of the current
#             # iteration is less than the target, in which case if that sum
#             # is closer to the target than the previous best difference, update
#             # it and then break to a higher number by i increasing
#             max_sum = num_i + nums[-1] + nums[-2]
#             if max_sum < target:
#                 if abs(max_sum - target) < abs(ans - target):
#                     ans = max_sum
#                 continue
#             # checking base case, which is if the minimum sum of the current
#             # iteration is greater than the target, in which case if that sum
#             # is closer to the target than the previous best difference, update
#             # it and then return the best difference, as all further iterations
#             # will only result in greater values, and thus worse differences
#             min_sum = num_i + nums[i + 1] + nums[i + 2]
#             if min_sum > target:
#                 return min_sum if abs(target - min_sum) < abs(target - ans) else ans
#             # initializing the two pointers, with left to the immediate right
#             # of i and right being at the end of the array
#             left = i + 1
#             right = len(nums) - 1
#             # standard loop looking through the array looking for the best sum, 
#             while left < right:
#                 # assigning sum to variable, avoid calculating multiple times
#                 three_sum = num_i + nums[left] + nums[right]
#                 # checking if the target has been found
#                 if three_sum == target:
#                     return target
#                 # updating the best sum if the difference of the current sum to 
#                 # the target is less than the best difference
#                 if abs(three_sum - target) < abs(ans - target):
#                     ans = three_sum
#                 # moving the left pointer to the right if element is too small
#                 if three_sum < target:
#                     left += 1
#                     # avoiding repeating the same element by checking if the 
#                     # previous element is the same, doen in right decrement too
#                     while left < len(nums) - 1 and nums[left] == nums[left - 1]:
#                         left += 1
#                 else:
#                     right -= 1
#                     # avoiding repeating the same element by checking if the 
#                     # previous element is the same, doen in right decrement too
#                     while right > i and nums[right] == nums[right + 1]:
#                         right -= 1
#         return ans


# test = [-1,2,1,-4]
test = [87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48, \
    30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,\
        45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,\
            -73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,\
                -10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,\
                    12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4]

sol = Solution()
print(sol.threeSumClosest(test, -275))