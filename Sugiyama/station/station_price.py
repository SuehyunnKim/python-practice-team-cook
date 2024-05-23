# 準備
import sys
args = sys.argv

#SELECT
from databace import session
from tables import stations

#引数を変数に渡す
station_1 = args[1]
station_2 = args[2]

#list
kilo_1 = session.query(stations).filter_by(name = station_1).first()
kilo_2 = session.query(stations).filter_by(name = station_2).first()

# #計算
answer = abs(kilo_1.kilo - kilo_2.kilo)

# #出力
print(str(answer))

