'''we use two min heaps to store free rooms and an array to count the
number of times a room is used. in each iteration, we free up rooms if possible. then assign the earliest room if avaialble, if not, we evacuate the earlest ending meeting and assign the meeting there.
'''
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        heapify(available)
        busy = [] #(end,room)
        count = [0] * n

        for start,end in meetings:
            # free up rooms
            while busy and busy[0][0] <= start:
                _,room = heappop(busy)
                heappush(available, room)
            
            if available:
                room = heappop(available)
                heappush(busy,(end,room))
                count[room] += 1
            else:
                end_time, room = heappop(busy)
                new_end = end_time + (end - start)
                heappush(busy,(new_end,room))
                count[room] += 1
        
        return count.index(max(count))