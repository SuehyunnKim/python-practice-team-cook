import sys

def calc_taxi_fee(distance):
  fee = 630
  if (distance > 1500):
    # distance of additional fee
    additional_dstnc = distance-1500
    if (additional_dstnc % 344 == 0):
      fee += (additional_dstnc//344)*98
    else:
      fee += (additional_dstnc//344 + 1)*98
  return fee

args = sys.argv
dstnc = int(args[1])
print(calc_taxi_fee(dstnc), end='')
