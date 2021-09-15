from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        if not nums:
            return []
        temp = random.choice(nums)
        LeftTemp = []
        RightTemp = []
        MidTemp = []
        for i in nums:
            if i > temp:
                RightTemp.append(i)
            elif i < temp:
                LeftTemp.append(i)
            elif i == temp:
                MidTemp.append(i)
        return self.sortArray(LeftTemp) + MidTemp + self.sortArray(RightTemp)






import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSortHelper(nums,0,len(nums)-1)
        return nums
    def shuffle_slice(self, a, start, stop):
        i = start
        while (i < stop-1):
            idx = random.randrange(i, stop)
            a[i], a[idx] = a[idx], a[i]
            i += 1
    def quickSortHelper(self, alist,first,last):
        if first<last:
            splitpoint = self.partition(alist,first,last)
            self.quickSortHelper(alist,first,splitpoint-1)
            self.quickSortHelper(alist,splitpoint+1,last)
    def partition(self, alist,first,last):        
        pivotindex = random.sample(range(first,last+1), 1)[0]
        temp = alist[pivotindex]
        alist[pivotindex] = alist[first]
        alist[first] = temp
        pivotvalue = alist[first]
        leftmark = first+1
        rightmark = last
        done = False
        while not done:        
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark += 1 
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark -= 1  
            if rightmark < leftmark:
                done = True
            else:
                temp = alist[rightmark]
                alist[rightmark] = alist[leftmark]
                alist[leftmark] = temp
        alist[first] = alist[rightmark]
        alist[rightmark] = pivotvalue
        return rightmark









        