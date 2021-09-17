from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
      # creating a helper function for reversing list when proper values are found
      def switch(i_left, i_right):
        nums[i_left], nums[i_right] = nums[i_right], nums[i_left] 
        nums[i_left+1:] = nums[i_left+1:][::-1]
      # find adjusted length and the element on the end of the input list
      length = len(nums)-1
      current = nums[length]
      # iterating until a decrease is found
      for i in range(1, length+1):
        # checking if a decrease has occured
        if nums[length-i] < current:
          # revisiting the array looking for the minimum value greter than the
          # element at the point of inflection
          element = nums[length-i]
          for j in range(1, i):
            index = length-i+j
            if element >= nums[index+1]:
              switch(length-i, length-i+j)
              return
          switch(length-i, length)
          return
        # if no decrease has occured, updating the current maximum
        else:
          current = nums[length-i]
      nums[:] = nums[::-1]
      return