class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num_arr = []
        num = 0
        power = 0
        while n > 0:
            mod = n % 10
            if mod != 0:
                num_arr.append(mod)
                num += mod * (10**power)
                power += 1
            n //= 10
        sum_ = sum(num_arr)

        return num*sum_ 