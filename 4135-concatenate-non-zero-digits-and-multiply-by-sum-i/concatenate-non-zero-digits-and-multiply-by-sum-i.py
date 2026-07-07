class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = 0
        power = 0
        sum_ = 0
        while n > 0:
            mod = n % 10
            if mod != 0:
                sum_ += mod
                num += mod * (10**power)
                power += 1
            n //= 10

        return num*sum_ 