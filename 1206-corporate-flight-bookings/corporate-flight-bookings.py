class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # differece array approach
        diff = [0] * n
        for start, end, seats in bookings:
            diff[start-1] += seats

            if end < n:
                diff[end] -= seats
        
        ans = [0] * n
        running = 0
        for i in range(n):
            running += diff[i]
            ans[i] = running
        
        return ans