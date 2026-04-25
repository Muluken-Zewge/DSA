'''we use sweep line with oredered map approach. we track the number of active bookings upto that point using a map(+1 for starting meeting, -1 for ending meeting), oreder it, sweep through and find the max.
'''
class MyCalendarThree:

    def __init__(self):
        self.active_changes = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.active_changes[startTime] += 1 # booking stated
        self.active_changes[endTime] -= 1 # booking ended

        active = 0
        max_active = 0
        for time in sorted(self.active_changes):
            active += self.active_changes[time]
            max_active = max(max_active,active)
        
        return max_active


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
