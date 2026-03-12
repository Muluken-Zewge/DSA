class FreqStack:

    def __init__(self):
        #count the number of occurances of each val
        self.counter = defaultdict(int)
        # store elements with the same count as groups
        self.stacks = defaultdict(list) 
        # number of times most occured val(s) occured
        self.max_count = 0 

    def push(self, val: int) -> None:
        #update counter
        self.counter[val] += 1
        # update max_count
        if self.counter[val] > self.max_count:
            self.max_count = self.counter[val]
        # update stacks
        self.stacks[self.counter[val]].append(val)

    def pop(self) -> int:
        # pop the most frequent value
        poped_val = self.stacks[self.max_count].pop()
        # update counter of popped val
        self.counter[poped_val] -= 1
        # update max_count
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return poped_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()