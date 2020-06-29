# Python program to print prime factors
import math
# prime
def primeFactors(n):
   # no of even divisibility
   while n % 2 == 0:
      print (2)
      n = n / 2
   # n reduces to become odd
   for i in range(3,round(math.sqrt(n)),2):
      # while i divides n
      while n % i== 0:
         print (i)
         n = n / i
   # if n is a prime
   if n > 2:
      print (n)
n = 600851475143 
primeFactors(n)