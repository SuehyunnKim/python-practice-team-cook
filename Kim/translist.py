import sys
from database import session
from tables import Transport

args = sys.argv
input_file_name = args[1]

transport_list=session.query(Transport).all()

with open(f'./output/{input_file_name}', mode='w', encoding='utf-8') as file:
  for data in transport_list:
      data_dict = data.__dict__
      dict_values = list(data.__dict__.values())
      dict_values.pop(0)
      for i in range(len(dict_values)):
        dict_values[i] = str(dict_values[i])
      file.write(f'{dict_values} \n')