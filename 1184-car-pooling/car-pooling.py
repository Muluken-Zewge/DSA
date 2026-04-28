class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for num, start, end in trips:
            events.append((start,num)) # pick up
            events.append((end,-num))  # drop off
        
        events.sort()
        curr_passengers = 0

        for _, num in events:
            curr_passengers += num
            if curr_passengers > capacity:
                return False
        
        return True