class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
    def productOnePass(self, nums: List[int]) -> List[int]:
        # initialize array for answer
        ans = [1] * len(nums)
        # creating variables that will hold product of all elements
        # to the right and left of current index respectively
        left, right = 1, 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
        return ans