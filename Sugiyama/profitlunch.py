#準備
import sys
args = sys.argv

#唐揚げ定食
chicken = 760

#カレーの値段
curry = 850

#引数を変数に渡す
chicken_order_num = int(args[1]) #唐揚げ定食の注文数
curry_order_num = int(args[2]) #カレーセットの注文数

#売上高計算
chicken_sales = chicken_order_num * 760 #唐揚げ定食
curry_sales = curry_order_num * 850 #カレーセット
sales = chicken_sales + curry_sales

#売上原価計算
chicken_prime_cost = round(chicken_sales * 0.323) #唐揚げ定食
curry_prime_cost = round(curry_sales * 0.284) #カレーセット
prime_cost = chicken_prime_cost + curry_prime_cost

#粗利計算
chicken_gross_cost = chicken_sales - chicken_prime_cost #唐揚げ定食
curry_gross_cost = curry_sales - curry_prime_cost #カレーセット
gross_cost = chicken_gross_cost + curry_gross_cost

#出力
print("売上高:" + str(sales) + "、" + "原価:" + str(prime_cost) + "、" + "粗利:" + str(gross_cost), end="")
