import sys

name_list = [
  "Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", 
  "Adachi", "Kuriyama", "Ohyama", "Kishida"
]
result_list = []

i = 1
while (i < len(name_list)):
  result_list.append(name_list[i])
  i += 2

print(result_list, end='')