import sys
num = int(sys.argv[1])

# 引数で与えられた値までの素数を判定してリストに入れる
prime = []
for i in range(2, num+1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        prime.append(i)

# 素数リストを一つずつ取り出して素因数分解
prime_factor = []

for k in prime:
    while num % k == 0:
        prime_factor.append(k)
        num = num / k
print(prime_factor)



