class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisor_sum = 0
        for num in nums:
            over = False
            divisors = set()
            i = 2
            while i <= sqrt(num):
                if num % i == 0:
                    if len(divisors) == 2:
                        over = True
                        break
                    else:
                        divisors.add(i)
                        divisors.add(num//i)
                i += 1
            if not over and len(divisors) == 2:
                divisor_sum = divisor_sum + 1 + num + sum(divisors)
            print("num: ",num)
            print("divisors: ",divisors)
            print("divisor_sum: ",divisor_sum)
        return divisor_sum