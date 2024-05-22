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

#唐揚げ定食の売上高を計算
chicken_price = (chicken * chicken_order_num)

#カレーセットの売上高を計算
curry_price = (curry * curry_order_num)

#売上高を足す
price = str(chicken_price + curry_price)

#出力しよう！
print(price, end="")