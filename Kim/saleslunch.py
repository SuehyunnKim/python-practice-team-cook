menu_info = {
  '唐揚げ定食': 760,
  'カレーセット': 850
}

import sys
args = sys.argv
order_cnt_1, order_cnt_2 = int(args[1]), int(args[2])

sales = menu_info['唐揚げ定食']*order_cnt_1 + menu_info['カレーセット']*order_cnt_2

print(sales, end='')

