



# class Leonardos:
#     def __init__(self, ):
#         self.n = n
#         self.prime_factors = []
#         self.prime_factorization()

#     def prime_factorization(self):
#         for i in range(2, self.n + 1):
#             if self.n % i == 0:
#                 self.prime_factors.append(i)
#                 self.n = self.n / i
#                 self.prime_factorization()
#                 break
#         return self.prime_factors

arg = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
sol = 1
for i in arg:
    sol *= i
print(sol)
print(10**18)