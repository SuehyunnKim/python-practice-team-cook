# リストの定義
name = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
name2= []

for i in range(0, len(name)): 
    if i %2 !=0:
        name2.append(name[i])
    
print(name2, end="")

