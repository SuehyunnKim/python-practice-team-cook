import sys
from datetime import date
from database import session
from tables import Transport

input_data = []
args = sys.argv
year = int(args[1][:4])
month = int(args[1][4:6])
day = int(args[1][6:])

input_date = date(year, month, day)
input_seq = int(args[2])
input_departure = args[3]
input_arrival = args[4]
input_via = args[5]
input_amount = int(args[6])

transport = Transport(
  date = input_date,
  seq = input_seq,
  departure = input_departure,
  arrival = input_arrival,
  via = input_via,
  amount = input_amount
)

try:
  session.add(transport)
  session.commit()
  print('交通費精算テーブルにデータを登録しました')
except:
  print('error:交通費精算テーブルにデータを登録できませんでした')