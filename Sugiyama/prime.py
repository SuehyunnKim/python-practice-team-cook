#準備
import sys
args = sys.argv

#引数を変数に渡す
n = int(args[1])


#関数を定義
def is_prime(n):
    if n <= 1:
        comment = "not"
        return comment
    elif n >= 1000:
        comment = "1000以上は判定できません"
        return comment
        
    for i in range (2, n):
        if n % i == 0:
            comment = "not"
            return comment
    comment = "prime"
    return  comment

print(is_prime(n), end="")