import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime, VARCHAR, DECIMAL
from database import Base
from database import ENGINE

# テーブル: Stations
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', VARCHAR(20))
    kilo = Column('kilo', DECIMAL(6,2))
    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)

# テーブル: Transport
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', VARCHAR(20))
    arrival = Column('arrival', VARCHAR(20))
    via = Column('via', VARCHAR(40))
    amount = Column('amount', Integer)
    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)

