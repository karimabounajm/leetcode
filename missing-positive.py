from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
      length = len(nums)
      if length == 0:
        return 1
      if length == 1:
        if nums[0] == 1:
          return 2
        else:
          return 1
      ticker = 0
      for i in range(length):
        ticker += 1
        # setting a buffer value to carry element parsed
        element = nums[i]
        # checking if the element should be rearranged in length init array
        if element < length and element > 0:
          ticker += 1
          while element < length and element > 0:
            print('firing')
            ticker += 1
            # extracting the element to be switched
            inner_element = nums[element]
            # checking if it itself should be switched
            if inner_element < length and inner_element > 0 and inner_element != element and inner_element != nums[inner_element]:
              print('firing1')
              nums[element] = nums[inner_element]
              nums[inner_element] = inner_element
            else:
              break
          element = nums[i]
          nums[i] = nums[element]
          if element >= length:
            nums[element] = 0
          else:
            nums[element] = element
      for i in range(1, length):
        ticker += 1
        if i != nums[i]:
          return abs(i)
      if length != nums[0]:
        return length
      else:
        return length + 1

nums = [5, 2, 3, -1, 9, 4, 12, 42, 19, 1, 0]
nums = [7,8,9,11,12]
nums = [3,4,-1,1]
nums = [1, 2, 6, 3, 4, 7, 5, 13, 16, 9, 0, 19, 8]
nums = [1,2,6,5,4,3]
nums = [0,2,1,1,1,1,3]
# nums = [0, 4, 2, 1, 5]
sol = Solution()
print(sol.firstMissingPositive(nums))
print(nums)