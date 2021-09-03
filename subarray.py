from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.helper_1(arr) % (10**9 + 7)
        elif k == 2:
            return self.helper2(arr) % (10**9 + 7)
        else:
            normal_max, augmented_max = self.helper_k(arr)
            if normal_max < 0:
                return 0
            elif augmented_max > normal_max:
                return (normal_max + (k-2) * (augmented_max - normal_max)) % (10**9 + 7)
            else:
                return normal_max % (10**9 + 7)  
    def helper_k(self, arr: List[int]):
        buffer_arr = 2*arr
        local_max = 0; global_max = -999999
        normal_max = 0; augmented_max = 0
        length = len(buffer_arr)
        for i in range(len(buffer_arr)):
            local_max = max(local_max + buffer_arr[i], buffer_arr[i])
            if(local_max > global_max):
                global_max = local_max
        arr = 3*arr; normal_max = global_max
        for i in range(length, len(arr)):
            local_max = max(local_max + arr[i], arr[i])
            if(local_max > global_max):
                global_max = local_max
        augmented_max = global_max
        return normal_max, augmented_max
    def helper_1(self, arr: List[int]):
        local_max = 0
        global_max = -999999
        for i in range(len(arr)):
            local_max = max(local_max + arr[i], arr[i])
            if(local_max > global_max):
                global_max = local_max
        if global_max < 0:
            return 0
        else:
             return global_max
    def helper2(self, arr: List[int]):
        arr = 2*arr
        local_max = 0
        global_max = -999999
        for i in range(len(arr)):
            local_max = max(local_max + arr[i], arr[i])
            if(local_max > global_max):
                global_max = local_max
        if global_max < 0:
            return 0
        else:
             return global_max


test = [10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
sol = Solution()
print(sol.kConcatenationMaxSum(test, 100000))