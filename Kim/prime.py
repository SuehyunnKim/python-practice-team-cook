import sys
import math

def is_prime(num):
  is_prime = 'Prime'
  for i in range(2, int(math.sqrt(num))+1):
    if (num % i == 0):
      is_prime = 'not'
      break
  return is_prime

args = sys.argv
n = float(args[1])

if (n<1000):
  output = is_prime(n)
else:
  output = '1000以上は判定できません'

print(output, end='')