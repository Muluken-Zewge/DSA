class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """we use bitmask to check if all the rows with reservations have
        free left, middle or right block to be allocated.the rows with no
        reservations has can sit two groups(left and right).
        """
        rows = defaultdict(int)
        for r,c in reservedSeats:
            rows[r] |= (1 << (c-1))

        # left block mask
        left_mask = 0
        for i in [2,3,4,5]:
            left_mask |= (1 << (i-1))

        # right block mask
        right_mask = 0
        for i in [6,7,8,9]:
            right_mask |= (1 << (i-1))  

        # middle block mask
        middle_mask = 0
        for i in [4,5,6,7]:
            middle_mask |= (1 << (i-1))   
        
        res = 0
        for r in rows:
            row_mask = rows[r]
            print(bin(row_mask)[2:])
            count = 0
            #check if left block is available
            if (row_mask & left_mask) == 0:
                count += 1
            #check if right block is available
            if (row_mask & right_mask) == 0:
                count += 1
            # If neither left nor right worked, try middle
            if count == 0 and (row_mask & middle_mask) == 0:
                count = 1

            res += count
        
        # include row with no reservations
        res += (n - len(rows)) * 2
        
        return res
