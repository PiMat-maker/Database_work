import psycopg2
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Enum
import enum


engine = create_engine('postgresql+psycopg2://pimat:pimat@db:5432/bakugan_db', echo=True)
Base = declarative_base()


class Side(enum.Enum):
    earth = "Earth"
    death_world = "Death World"


class Space(enum.Enum):
    pyrus = "Pyrus"
    terra = "Terra"
    aquas = "Aquas"
    darkus = "Darkus"
    haos = "Haos"
    ventus = "Ventus"


association_table_battles = Table('association_battles', Base.metadata,
    Column("battle_id", ForeignKey("battles.id"), primary_key=True),
    Column("hero_id", ForeignKey("heroes.id"), primary_key=True),
    Column("hero_moto_id", ForeignKey("hero_motos.id"), primary_key=True)
)


class Heroes(Base):

    __tablename__ = "heroes"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    side = Column(Enum(Side))
    name = Column(String(40), nullable=False, unique=True)
    space = Column(Enum(Space))
    force = Column(Integer)
    moto = relationship("Hero_motos", back_populates="hero")
    battles = relationship("Battles", secondary=association_table_battles, back_populates="hero")

    def __str__(self) -> str:
        return f'Hero name: {self.name}, space: {self.space}, side: {self.side}, force = {self.force}G'


class Hero_motos(Base):

    __tablename__ = "hero_motos"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id = Column(Integer, ForeignKey("heroes.id", ondelete='CASCADE'))
    moto_id = Column(Integer)
    moto = Column(String(100))
    hero = relationship("Heroes", back_populates="moto")
    battles = relationship("Battles", secondary=association_table_battles, back_populates="moto", overlaps="battles")

    def __str__(self) -> str:
        return f"Hero's moto is {self.moto}"


class Battles(Base):

    __tablename__ = "battles"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero = relationship("Heroes",  secondary=association_table_battles, back_populates="battles", overlaps="battles")
    moto = relationship("Hero_motos",  secondary=association_table_battles, back_populates="battles", overlaps="battles,hero")
    hero_1_id = Column(Integer, ForeignKey("heroes.id"))
    hero_1_moto_id = Column(Integer, ForeignKey("hero_motos.id"))
    hero_2_id = Column(Integer, ForeignKey("heroes.id"))
    hero_2_moto_id = Column(Integer, ForeignKey("hero_motos.id"))
    winner = Column(Integer)

    def __str__(self) -> str:
        battle_result = "Draw"
        if self.winner == 1:
            battle_result = f"Winner {self.hero_1_id}"
        elif self.winner == 2:
            battle_result = f"Winner {self.hero_2_id}"
        return f'{self.hero_1_id} vs {self.hero_2_id} | Result: {battle_result}'


class Hero_stories(Base):

    __tablename__ = "hero_stories"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero = relationship("Heroes", backref=backref("hero_stories", uselist=False))
    hero_id = Column(Integer, ForeignKey("heroes.id", ondelete='CASCADE'))
    story = Column(String(1000))

    def __str__(self):
        return f"Hero id: {self.hero_id}\n{self.story}"