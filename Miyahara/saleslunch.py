import sys

# 唐揚げとカレーの注文数
karaage_num = int(sys.argv[1])
curry_num = int(sys.argv[2])

karaage_price = 760
curry_price = 850

sales = (karaage_num * karaage_price) + (curry_num * curry_price)

print(sales, end="")
    

