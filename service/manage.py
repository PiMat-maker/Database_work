import click
from create_db import Base, engine
from sqlalchemy.orm import sessionmaker
from seed import seed_Heroes, seed_Hero_motos, seed_Hero_stories, seed_Battles
from ddl_funcs import add_hero, add_hero_moto, add_hero_story, run_battle, delete_hero



@click.group()
def cli():
    pass


@cli.command("create_db")
def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@cli.command("seed_db")
def seed_db():
    Session = sessionmaker(bind=engine)
    seed_Heroes(Session)
    seed_Hero_motos(Session)
    seed_Hero_stories(Session)
    seed_Battles(Session)


@cli.command("add_hero")
def add_db_hero():
    Session = sessionmaker(bind=engine)
    add_hero(Session)


@cli.command("add_moto")
def add_db_hero_moto():
    Session = sessionmaker(bind=engine)
    add_hero_moto(Session)


@cli.command("add_story")
def add_db_hero_story():
    Session = sessionmaker(bind=engine)
    add_hero_story(Session)


@cli.command("run_battle")
def add_db_battle():
    Session = sessionmaker(bind=engine)
    run_battle(Session)


@cli.command("delete_hero")
def delete_db_hero():
    Session = sessionmaker(bind=engine)
    delete_hero(Session)


if __name__ == "__main__":
    cli()