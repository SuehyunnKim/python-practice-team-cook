import sys

# 引数を受け取る
num = int(sys.argv[1])

# 絶対値に変更
absolute_num = abs(num)

print("{} {}".format(num, absolute_num), end="")