import sys
from tables import Transport
from database import session
import os

file_name = sys.argv[1]

# データの抽出
translist = session.query(Transport).all()

# パスの生成、ファイル名を引数で与えられたものにする
path = os.path.join("..","..","files","{}".format(file_name))

# ファイルにデータを書き出す
with open(path, 'w') as f:
    for record in translist:
        f.write('"{}","{}","{}","{}","{}","{}"\n'.format
                (record.date, record.seq, record.departure, record.arrival, record.via, record.amount))
    

