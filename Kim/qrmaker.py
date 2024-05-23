import sys
import qrcode

# path_of_qrlist = '/home/matcha-23training/practice/python-practice-team-cook/Kim/test_files/qrlist.txt'
args = sys.argv
path_of_qrlist = args[1]

with open(path_of_qrlist, 'rt', encoding='utf-8') as f:
  read_lines = f.readlines()

  for line in read_lines:
    line.rstrip()
    url_split = line.split('.')

    if (line.startswith('https://www')):
      name = url_split[1]
    else:
      name = url_split[0]

    qr_url = line
    qr_img = qrcode.make(qr_url)

    save_path = f'./output/{name}.png'
    qr_img.save(save_path)

# example code
# new_qr = qrcode.make('https://www.google.com')
# new_qr.save('./output/google.png')