class Solution:
    def minimumDeletions(self, s: str) -> int:
        # in each index, the sum of the number of b's to the left and the number of a's to the right gives us the number of deletions and take the minimum over the entire array
        n = len(s)
        b_count_left = 0
        a_count_right = s.count('a') #total count of a
        res = n

        for i in range(n):
            # modify a_count
            if s[i] == 'a':
                a_count_right -= 1
            deletion = a_count_right + b_count_left
            res = min(res,deletion)

            #modify b_count for next iteration
            if s[i] == 'b':
                b_count_left += 1
        
        return res