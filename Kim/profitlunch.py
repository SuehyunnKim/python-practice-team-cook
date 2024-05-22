import sys

menu_info = {
  '唐揚げ定食': {
    'price': 760,
    'cost_rate': 0.323
  },
  'カレーセット': {
    'price': 850,
    'cost_rate': 0.284
  }
}

# Class for calculating sales, cost and profit of each product
class Calculation:
  def __init__(self, product, order_cnt):
    self.product = product
    self.order_cnt = order_cnt

  def calc_sales(self):
    sales = menu_info[self.product]['price']*self.order_cnt
    return sales

  def calc_cost(self):
    sales = self.calc_sales()
    cost = round(sales*menu_info[self.product]['cost_rate'])
    return cost
  
  def calc_profit(self):
    sales = self.calc_sales()
    cost = self.calc_cost()
    profit = sales - cost
    return profit
  
args = sys.argv
order_cnt_1 = int(args[1])
order_cnt_2 = int(args[2])

# Create instance of Calculation
karaage = Calculation('唐揚げ定食',order_cnt_1)
curry = Calculation('カレーセット', order_cnt_2)

# Calculate sales, cost and profit of 唐揚げ定食
karaage_sales = karaage.calc_sales()
karaage_cost = karaage.calc_cost()
karaage_profit = karaage.calc_profit()

# Calculate sales, cost and profit of カレーセット
curry_sales = curry.calc_sales()
curry_cost = curry.calc_cost()
curry_profit = curry.calc_profit()

# Total sales, cost and profit
total_sales = karaage_sales + curry_sales
total_cost = karaage_cost + curry_cost
total_profit = karaage_profit + curry_profit

print(f'売上高：{total_sales}、原価：{total_cost}、粗利：{total_profit}', end='')