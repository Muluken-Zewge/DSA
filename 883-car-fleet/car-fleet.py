class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if a car further from target reach the target before/at equal time with a car closer to the target, they form a fleet

        cars = []
        stack = [] # holds the time it took for each fleet to reach the target
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        # sort in asending order(furthest -> nearest)
        cars.sort(reverse=True)

        for pos,spd in cars:
            time = (target - pos) / spd
            # further car reach target before/equally with near car->a fleet
            if stack and time <= stack[-1]:
                continue

            stack.append(time) # new fleet formed
            
        return len(stack)

        