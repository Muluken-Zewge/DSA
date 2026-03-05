class Solution:
    def minOperations(self, s: str) -> int:
        # case 1: start with 0
        case1_prev = '1'
        case1_min = 0
        for bit in s:
            if case1_prev == '0' and bit == '0':
                case1_min += 1
                case1_prev = '1'
            elif case1_prev == '1' and bit == '1':
                case1_min += 1
                case1_prev = '0'  
            elif case1_prev != bit:
                case1_prev = bit     
        
        # case 2: start with 1
        case2_prev = '0'
        case2_min = 0
        for bit in s:
            if case2_prev == '0' and bit == '0':
                case2_min += 1
                case2_prev = '1'
            elif case2_prev == '1' and bit == '1':
                case2_min += 1
                case2_prev = '0'  
            elif case2_prev != bit:
                case2_prev = bit  
        
        return min(case1_min,case2_min)
