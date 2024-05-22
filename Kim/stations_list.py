from database import session
from tables import Stations

# データを取得する
stations_list=session.query(Stations).all()

for station in stations_list:
    print(station.seq, station.name, station.kilo)