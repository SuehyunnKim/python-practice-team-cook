import sys
distance = int(sys.argv[1])
base = 1500
initial_fare = 630
afterwards = 344
afterwards_fare = 98

# 与えられた距離が初乗りか判定
if (distance <= base):
    fare = initial_fare
else:
    after = distance - base 
    # 初乗りを超えた文を計算
    if (after % afterwards == 0):
        total_after = afterwards_fare * (after // afterwards)
    else:
        total_after = afterwards_fare * (after // afterwards +1)

    fare = initial_fare + total_after

print(fare, end="")