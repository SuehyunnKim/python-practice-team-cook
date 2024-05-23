import sys
num = int(sys.argv[1])

# 入力値が1000以上だったら処理を止める
if num >= 1000:
    print("1000以上は判定できません", end="")
    sys.exit()

# 2から入力値の前まで数で割る、割り切れたら終了、割り切れなかったら素数
for i in range(2,num):
    if (num  % i == 0):
        print("not", end="")
        break
    else:
        print("Prime", end="")
        break 
