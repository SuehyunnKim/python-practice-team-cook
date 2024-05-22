from database import session
from tables import Stations

stations_arr = [
  [1,'東京',0.00],
  [2,'品川',6.78],
  [3,'新横浜',25.54],
  [4,'名古屋',342.02],
  [5,'京都',476.31],
  [6,'新大阪',515.35]
]

#INSERT処理
session.add_all([Stations(seq=station[0],name=station[1],kilo=station[2]) 
              for station in stations_arr])
#コミット
session.commit()