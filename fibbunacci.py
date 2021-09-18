class Solution:
    def fib_bottom(self, N: int) -> int:
        if (N <= 1):
            return N

        current = 1
        prev1 = 1
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(3, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
    def fib_golden(self, N: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))