#準備
import sys
args = sys.argv

#SELECT
from database import session
from tables import transport

#引数入力
date = args[1]
seq  = args[2]
departure = args[3]
arrival = args[4]
via = args[5]
amount = args[6]

