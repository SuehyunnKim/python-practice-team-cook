#準備
import sys
args = sys.argv

#名前のリスト
name_list = ["Kurita", "Tanaka", "kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

#奇数が添え字のお名前をぶち込むための空のリスト
empty_list = []

#お名前をこねくり回す
i = 1 #iに先に1を入れておく

while i < len(name_list):
    empty_list.append(name_list[i])
    i += 2
print(empty_list)