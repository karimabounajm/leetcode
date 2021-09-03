from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sorting intervals by starting time (automatically first element)
        intervals.sort()
        # initilaizing array for currently used rooms, first element is the 
        # end time of the earliest meeting
        usedroom=[intervals[0][1]]
        for i in range(1, len(intervals)): 
            # checking if the ending time of the first occupied room that 
            # would be over is before the start of the the current meeting
            if usedroom[0]<= intervals[i][0]:
                # removing the meeting that has ended if it has an ending 
                # time that is before the start of the current meeting
                heapq.heappop(usedroom)
            # inserting the current meeting into the minheap, which is 
            # sorted by the end time of the meeting
            heapq.heappush(usedroom, intervals[i][1])
        # returning how meetings are there. this works because only one
        # meeting is removed whenever an already started meeting is shown
        # to end
        return len(usedroom)
    
    def minMeetingRoomsSlow(self, intervals: List[List[int]]) -> int:
        # checking if meetings exist
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        # initializing the free room object as an array
        free_rooms = []
        # sorting the intervals by their starting time
        intervals.sort(key= lambda x: x[0])
        print(intervals)
        # turning free room object into a heap, noting that the
        # first element is the end time of the earliest meeting
        heapq.heappush(free_rooms, intervals[0][1])
        # creating variable that holds the maximum number of rooms ever
        # occupied at a given instance
        max_rooms = 1
        # iterating through the intervals, with the point of the loop
        # being to check if every meeting by increasing starting time
        # whether or not a meeting is free given a min heap of values
        # inserted in order of start time and sorted by their end time
        for i in intervals[1:]:
            # checking if a given room, which is hosting a meeting that had 
            # to have started before the one in the itereation, is ended
            while free_rooms and free_rooms[0] <= i[0]:
                # if a room hosts a meeting that ends before the start of the
                # current one in the array, it is removed from the heap
                heapq.heappop(free_rooms)
            # inserting the new meeting into a room
            heapq.heappush(free_rooms, i[1])
            if len(free_rooms) > max_rooms:
                max_rooms = len(free_rooms)
        return max(len(free_rooms), max_rooms)


test = [[1, 2], [0,30],[5,10], [16, 21], [4, 49], [15,20]]
sol = Solution()
print(sol.minMeetingRooms(test))  