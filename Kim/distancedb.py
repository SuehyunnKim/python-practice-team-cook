import sys
from database import session
from tables import Stations

args = sys.argv
input_station_1 = args[1]
input_station_2 = args[2]

def get_dstnc(station):
  data = session.query(Stations.kilo).filter_by(name = station).first()
  return data.kilo

dstnc_btw_stations = abs(get_dstnc(input_station_1) - get_dstnc(input_station_2))
print(dstnc_btw_stations)