import sys
from decimal import Decimal, ROUND_HALF_UP
karaage_num = int(sys.argv[1])
curry_num = int(sys.argv[2])

karaage_price = 760
curry_price = 850

# 売上高を算出
karaage_sales = karaage_num * karaage_price
curry_sales = curry_num * curry_price
sales = karaage_sales + curry_sales

# 原価を算出
karaage_cost = karaage_sales * 0.323
curry_cost = curry_sales * 0.284
karaage_cost = Decimal(karaage_cost).quantize(Decimal("1"),rounding = ROUND_HALF_UP)
curry_cost = Decimal(curry_cost).quantize(Decimal("1"),rounding = ROUND_HALF_UP)
cost = karaage_cost + curry_cost

# 粗利を算出
profit = sales - cost

print("売上高：{}、原価：{}、粗利：{}".format(sales,cost,profit), end="")

