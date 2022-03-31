import logging
import psycopg2
from create_db import Heroes, Hero_motos, Side
import random
from math import exp


def randomize_number(limit: int) -> int:
    return int(limit*random.random())


def choose_side(without_sides: set[Side]) -> Side:

    actual_sides: list[Side] = [side for side in list(Side) if side not in without_sides]
    number_sides: int = len(actual_sides)

    index_side: int = randomize_number(number_sides)
    
    return actual_sides[index_side]


def choose_hero(side: Side, Session) -> Heroes:
    with Session() as session:
        heroes: list[Heroes] = session.query(Heroes).filter(Heroes.side == side).all()

    number_heroes: int = len(heroes)

    index_hero: int = randomize_number(number_heroes)

    return heroes[index_hero]


def choose_moto(hero: Heroes, Session) -> Hero_motos | None:
    with Session() as session:
            motos: list[Hero_motos] = session.query(Hero_motos).filter(Hero_motos.hero_id == hero.id).all()

    number_motos: int = len(motos)

    try:
        index_moto: int = randomize_number(number_motos)
        moto: Hero_motos = motos[index_moto]
    except IndexError:
        logging.warn(f"No any moto for {hero}")
        return None

    return moto
    


def count_puasson_distibution(coef_lambda: float) -> float:
    return exp(-coef_lambda) * coef_lambda