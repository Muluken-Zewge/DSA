class FreqStack:

    def __init__(self):
        #count the number of occurances of each val
        self.counter = defaultdict(int)
        # store elements with the same count as groups
        self.stacks = defaultdict(list) 
        # number of times most occured val(s) occured
        self.max_freq = 0 

    def push(self, val: int) -> None:
        #update counter
        count = self.counter[val] + 1
        self.counter[val] = count
        # update max_freq
        if count > self.max_freq:
            self.max_freq = count
        # update stacks
        self.stacks[count].append(val)

    def pop(self) -> int:
        # pop the most frequent value
        poped_val = self.stacks[self.max_freq].pop()
        # update counter of popped val
        self.counter[poped_val] -= 1
        # update max_freq
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return poped_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()