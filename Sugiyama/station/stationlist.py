from databace import session
from tables import stations

holidaylist = session.query(stations).all()

for station in stations:
    print(station.seq,station.name,station.kilo)