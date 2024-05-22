#準備
import math 
import sys
args = sys.argv

#引数を変数に入れる(距離の意)
distance = int(args[1])

#初乗り1500mまでの料金を変数に入れる(初乗りの意)
starting = 630

#以後344mごとの料金98円を変数に入れる(走行の意)
driving = 0

#1500mかどうかを判定
if distance <= 1500:
    price_x = starting
    print(str(price_x), end="")
else:
    remainder_distance = distance - 1500 #余りの距離の意 #初乗りの距離を抜く
    x = remainder_distance / 344 #先に割った結果を変数へ渡す
    if remainder_distance % 344 == 0 : #距離の割り算の意 #もし344で割り切れたら…
        price_x = (x * 98) + 630 #余りの距離は98の何個分かを割り算で導き出し、初乗り料金を足す
    else: #割り切れない場合...
        price_x = ((x + 1) * 98) + 630 # 例) (0.85 * 98) + 630 の場合結果が0になってしまうため1を足す
        #計算結果を小数点が表示されないように整数に変換
        price = math.floor(price_x)

        #文字型にして出力
        print(str(price), end="")
