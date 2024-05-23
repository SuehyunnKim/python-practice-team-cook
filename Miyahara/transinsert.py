import sys
from datetime import date
from database import session
from tables import Transport 
import datetime


# 引数を受け取る
date = sys.argv[1]
seq = int(sys.argv[2])
departure = sys.argv[3]
arrival = sys.argv[4]
via = sys.argv[5]
amount = int(sys.argv[6])

year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8]) 

dt = datetime.date(year, month, day)

# テーブルのデータを抽出後、引数と同じdata, seqだった場合の処理
transport_dateget = session.query(Transport).filter_by(date = dt).order_by(Transport.date.desc()).first()
transport_seqget = session.query(Transport).filter_by(seq = seq).order_by(Transport.seq.desc()).first()

if transport_dateget != None or transport_seqget != None:
    if transport_dateget.date == dt or transport_seqget.seq == seq:
        print("交通費テーブルにデータを登録できませんでした")
        sys.exit()


# 引数で与えられたデータをデータベースに登録
tranceport = Transport(
    date = dt,
    seq = seq,
    departure = departure, 
    arrival = arrival,
    via = via,
    amount = amount,
)

session.add(tranceport)
session.commit()
print("交通費精算テーブルにデータを登録しました")

    



