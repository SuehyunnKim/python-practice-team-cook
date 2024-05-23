import sys
# 祝日データの取り込み
from database import session
from tables import Stations

# 引数を受け取る
sta1 = sys.argv[1]
sta2 = sys.argv[2]

# データベースから引数と一致する値を取り出す
get_sta1 = session.query(Stations).filter_by(name = sta1).first()
get_sta2 = session.query(Stations).filter_by(name = sta2).first()

# 取り出した値で距離を求める
result = abs(round((get_sta2.kilo - get_sta1.kilo),2))
print(result, end="")