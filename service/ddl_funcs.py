import psycopg2
from sqlalchemy import func
from create_db import Heroes, Hero_motos, Hero_stories, Battles, Side, Space
import random
from battle_utils import choose_hero, choose_side, choose_moto, count_puasson_distibution


def confirm_input_value(field: str, value_field: str) -> bool:
    confirmation: str = input(f"So, {field} is {value_field}.\n Is that right? (Y/N)")

    return len(confirmation) > 0 and confirmation[0].lower() == 'y'


def input_side() -> Side:
    result_side: Side | None = None

    while not result_side:
        try:
            result_side = Side(input(f"Input one of sides: {[side.value for side in list(Side)]}\n"))
        except ValueError:
            print("Wrong side name")

    return result_side


def input_str(field: str) -> str:
    value_field: str = ''

    while value_field == '':
        value_field = input(f"Input {field}:\n")
        
        if not confirm_input_value(field, value_field):
            value_field = ''

    return value_field


def input_space() -> Space:
    result_space: Space | None = None

    while not result_space:
        try:
            result_space = Space(input(f"Input one of spaces: {[space.value for space in list(Space)]}\n"))
        except ValueError:
            print("Wrong space name")

    return result_space


def input_force() -> int:
    force: int = -1

    while force <= 0:
        try:
            force = int(input("Input hero's force value :\n"))

            if force <= 0:
                raise ValueError()
        except ValueError:
            print("Wrong force value. Value should be positive and more than 0\n")
        else:
            if not confirm_input_value("hero's force", str(force)):
                force = -1
        
    return force


def get_hero_by_name(heroes_query: list[Heroes]) -> Heroes | None:
    """
    Return a hero if there is a such hero's name in database. Else return None
    """
    print(f"Valid hero's names: {[hero.name for hero in heroes_query.all()]}")
    hero_name = input_str("hero's name")
    
    heroes: list[Heroes] = heroes_query.filter(Heroes.name == hero_name).all()

    if len(heroes) == 1:
        return heroes[0]

    print("Wrong hero's name")
    
    return None


def add_instance(Session, instance: Heroes | Hero_motos | Hero_stories | Battles) -> None:
    with Session() as session:
        session.add(instance)
        session.commit()


def delete_instance(Session, instance: Heroes | Hero_motos | Hero_stories | Battles) -> None:
    with Session() as session:
        session.delete(instance)
        session.commit()
    

def add_hero(Session) -> None:
    name = input_str("hero's name")
    side = input_side()
    space = input_space()
    force = input_force()

    new_hero = Heroes(
        name=name, 
        side=side, 
        space=space, 
        force=force
    )

    add_instance(Session, new_hero)


def add_hero_moto(Session) -> None:
    with Session() as session:
        heroes_query: list[Heroes] = session.query(Heroes)

    hero: Heroes | None = None
    
    while not hero:
        hero = get_hero_by_name(heroes_query)

    moto: str = input_str("hero's moto")

    with Session() as session:
        hero_motos_max_id: int | None = session.query(func.max(Hero_motos.moto_id)).filter(Hero_motos.hero_id == hero.id).first()[0]

    if hero_motos_max_id is None:
        hero_motos_max_id = 0

    new_hero_moto: Hero_motos = Hero_motos(
        hero_id=hero.id, 
        moto_id=hero_motos_max_id + 1, 
        moto=moto
    )

    add_instance(Session, new_hero_moto)


def add_hero_story(Session) -> None:
    with Session() as session:
        heroes_query: list[Heroes] = session.query(Heroes)

    hero: Heroes | None = None
    
    while not hero:
        hero = get_hero_by_name(heroes_query)

    story: str = input_str("hero's story")

    new_hero_story: Hero_stories = Hero_stories(
        hero_id=hero.id,
        story=story
    )

    add_instance(Session, new_hero_story)


def delete_hero(Session) -> None:
    with Session() as session:
        heroes_query: list[Heroes] = session.query(Heroes)

    hero: Heroes | None = None
    
    while not hero:
        hero = get_hero_by_name(heroes_query)

    session.close_all()
    
    delete_instance(Session, hero)


def run_battle(Session) -> None:
    first_side: Side = choose_side(set())
    second_side: Side = choose_side({first_side})

    first_hero: Heroes = choose_hero(first_side, Session)
    second_hero: Heroes = choose_hero(second_side, Session)

    first_hero_moto: Hero_motos = choose_moto(first_hero, Session)
    second_hero_moto: Hero_motos = choose_moto(second_hero, Session)

    draw_probability = count_puasson_distibution(first_hero.force / second_hero.force)
    first_win_probability = (1 - draw_probability) * first_hero.force / (first_hero.force + second_hero.force)
    second_win_probability = 1 - draw_probability - first_win_probability

    result_probability = random.random()
    winner: int = 0

    if first_win_probability > result_probability:
        winner = 1
    elif first_win_probability + second_win_probability > result_probability:
        winner = 2

    new_battle = Battles(
        hero_1_id=first_hero.id,
        hero_1_moto_id=first_hero_moto.id,
        hero_2_id=second_hero.id, 
        hero_2_moto_id=second_hero_moto.id, 
        winner=winner
    )

    add_instance(Session, new_battle)


def main():
    return


if __name__ == "__main__":
    main()