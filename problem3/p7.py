# 7. Reverse Integer

#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Solution:

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        limit = 2**31 - 1 if sign == 1 else 2**31
        max_div = limit // 10
        max_digit = limit % 10

        result = 0
        while x:
            digit = x % 10
            x //= 10

            if result > max_div or (result == max_div and digit > max_digit):
                return 0

            result = result * 10 + digit

        return sign * result

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.reverse(123))
#     print(sol.reverse(-123))
#     print(sol.reverse(120))