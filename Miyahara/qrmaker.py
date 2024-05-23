import sys
import qrcode
import os

# 引数にパスを受け取る
read_file = sys.argv[1]

# 受け取るURLのリストを作成
urls = []

# 指定されたパスのファイルを開く
with open(read_file, mode="r") as f:
    for line in f:
        urls.append(line.replace("\n", ""))

# 作成するファイル名の初期化
file_num = 1

# URLsリストからQRコードを出力
for url in urls:
    make_path = os.path.join("..","..","files","{}.png".format(file_num))
    img = qrcode.make(url)
    img.save(make_path)
    file_num += 1