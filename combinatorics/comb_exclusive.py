from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # creating a recursive nest function
        def dfs(current, array, index):
            if current == 0:
                ans.append(array)
            for i in range(index, len(candidates)):
                # print(candidate, i)
                if candidates[i] > current:
                    break
                elif candidates[i] == current:
                    ans.append(array + [candidates[i]])
                    break
                else:
                    dfs(current-candidates[i], array + [candidates[i]], i)
            
        ans = []
        candidates = sorted(set(candidates))
        print(candidates)
        dfs(target, [], 0)
        return ans
        
nums = [4, 5, 6, 3, 8]
tar = 11
sol = Solution()
print(sol.combinationSum(nums, tar))
print(nums)