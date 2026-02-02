class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisor_sum = 0
        for num in nums:
            divisors = set()
            i = 2
            while i <= sqrt(num):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num//i)
                if len(divisors) > 2:
                    break

                i += 1
            if len(divisors) == 2:
                divisor_sum = divisor_sum + 1 + num + sum(divisors)
           
        return divisor_sum