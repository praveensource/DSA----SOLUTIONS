class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # with loops
        # if n <= 0:
        #     return False

        # i = 0 
        # while 4 ** i <= n:
        #     if 4 ** i == n:
        #         return True
        #     i += 1
        # return False

        # without loops 
        # 4 is also a power of 2 and we check if given is power of 2 
        # and also we check if we have number or bit is even at tht positions ie it should be zero
        # Tc and sc o(1), o(1)
        return n > 0 and (n & (n - 1) == 0) and (n - 1) % 3 == 0

