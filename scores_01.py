import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///scorers_01.db')
Base = declarative_base()


class Leaders(Base):
    __tablename__ = 'scoring_leaders_2001'
    id = Column(Integer, primary_key=True)
    rank = Column("Rank", Integer)
    player = Column("Player", String)
    team = Column("Team", String)
    games = Column("Games", Integer)
    points = Column("Points", Integer)
    average = Column("Average_points", Float)
    per_40_min =Column("Average_playing_minutes", Float)

    def __init__(self,rank,player,team, games,points,average,per_40_min):
        self.rank = rank
        self.player = player
        self.team = team
        self.games = games
        self.points = points
        self.average = average
        self.per_40_min = per_40_min

    def __repr__(self):
        return f"{ self.rank} { self.player} {self.team} {self.games} {self.points} {self.average} { self.per_40_min}"

Base.metadata.create_all(engine)
