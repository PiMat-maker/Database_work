import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Heroes, Hero_motos, Hero_stories, Side, Space
from ddl_funcs import run_battle

def seed_Heroes(Session):
    dan = Heroes(side=Side.earth, name="Dan", space=Space.pyrus, force=890)
    shun = Heroes(side=Side.earth, name="Shun", space=Space.ventus, force=920)
    runo = Heroes(side=Side.earth, name="Runo", space=Space.haos, force=850)
    mask = Heroes(side=Side.death_world, name="The Mask", space=Space.darkus, force=950)
    deisy = Heroes(side=Side.death_world, name="Deisy", space=Space.terra, force=830)
    marucho_clone = Heroes(side=Side.death_world, name="Marucho clone", space=Space.aquas, force=870)

    with Session() as session:
        session.add(dan)
        session.add(shun)
        session.add(runo)
        session.add(mask)
        session.add(deisy)
        session.add(marucho_clone)
        session.commit()


def seed_Hero_motos(Session):
    dan_moto_1 = Hero_motos(hero_id=1, moto_id=1, moto="Drago is on the field")
    dan_moto_2 = Hero_motos(hero_id=1, moto_id=2, moto="Saurus appears")
    shun_moto_1 = Hero_motos(hero_id=2, moto_id=1, moto="Skyress is on the field")
    shun_moto_2 = Hero_motos(hero_id=2, moto_id=2, moto="Highlash join")
    runo_moto_1 = Hero_motos(hero_id=3, moto_id=1, moto="Tigrerra is on the field")
    runo_moto_2 = Hero_motos(hero_id=3, moto_id=2, moto="Open the gate card")
    mask_moto_1 = Hero_motos(hero_id=4, moto_id=1, moto="Hydronoid is on the field")
    mask_moto_2 = Hero_motos(hero_id=4, moto_id=2, moto="Reaper reapers")
    deisy_moto_1 = Hero_motos(hero_id=5, moto_id=1, moto="Claive is on the field")
    deisy_moto_2 = Hero_motos(hero_id=5, moto_id=2, moto="The force of terra")
    marucho_clone_moto_1 = Hero_motos(hero_id=6, moto_id=1, moto="Froggy is on the field")
    marucho_clone_moto_2 = Hero_motos(hero_id=6, moto_id=2, moto="Tsunami")

    with Session() as session:
        session.add(dan_moto_1)
        session.add(dan_moto_2)
        session.add(shun_moto_1)
        session.add(shun_moto_2)
        session.add(runo_moto_1)
        session.add(runo_moto_2)
        session.add(mask_moto_1)
        session.add(mask_moto_2)
        session.add(deisy_moto_1)
        session.add(deisy_moto_2)
        session.add(marucho_clone_moto_1)
        session.add(marucho_clone_moto_2)
        session.commit()


def seed_Hero_stories(Session):
    dan_story = Hero_stories(hero_id=1, story="Dan is the main human protagonist in the series, who, is 12 years old (11 in the Japanese dub) in the first season, 15 in New Vestroia, 16 in Gundalian Invaders, and 17 in Mechtanium Surge. In the beginning he is ranked #121, and by episode 39, he is ranked #1, and has become ranked #4 or under in episode 6 of Mechtanium Surge.")
    shun_story = Hero_stories(hero_id=2, story="Shun is 13 years old (11 in the Japanese dub), has black hair, which is tied into a long ponytail, bronze-brown eyes and wears a purple jacket over a dark, dark blue (almost black) sleeveless shirt. He is a master of Bakugan and co-created the rules with Dan. He is also Dan's childhood best friend. Shun is a loner, a boy of very few words, but yet is willing to help his friends at almost every turn. He is a Ventus brawler and he approaches Bakugan like a ninja.")
    runo_story = Hero_stories(hero_id=3, story="Runo is a 12-year-old (11 in the Japanese dub) girl who loves playing Bakugan against skilled people so she can show off. Runo is a Haos brawler. Her Guardian Bakugan is a Haos Tigrerra (the others being Terrowclaw and Saurus), who is very obedient and powerful in battle.")
    mask_story = Hero_stories(hero_id=4, story="Alice(The Mask) is a 14-year-old girl from Moscow, Russia. Although she knows almost everything about the game, she rarely plays it; she is generally afraid of hurting others, including Bakugan. She usually just gives advice to the other brawlers, which she prefers over battling. Alice is kind and caring, worried forand compassionate towards others and does not think of herself. She also adores Shun. Alice was sometimes unconsciously possessed by 'Masquerade' (her mysterious alter-ego)")
    deisy_story = Hero_stories(hero_id=5, story="Older sister of Julie")
    marucho_clone_story = Hero_stories(hero_id=6, story="Marucho loves to play Bakugan and is also able to change attributes. Marucho is eleven (ten in the Japanese dub) and is an aquas brawler. He is seen after being defeated by Volt in episode 13, being held as a hostage in episodes 15 and 17, and was later freed by Mira and Spectra in episode 20, even though he is unaware of this.")

    with Session() as session:
        session.add(dan_story)
        session.add(shun_story)
        session.add(runo_story)
        session.add(mask_story)
        session.add(deisy_story)
        session.add(marucho_clone_story)
        session.commit()


def seed_Battles(Session):
    for i in range(20):
        run_battle(Session)


def main():

    engine = create_engine('postgresql+psycopg2://pimat:pimat@db:5432/bakugan_db', echo=True)
    Session = sessionmaker(bind=engine)
    seed_Heroes(Session)
    seed_Hero_motos(Session)
    seed_Hero_stories(Session)
    seed_Battles(Session)

if __name__ == "__main__":
    main()