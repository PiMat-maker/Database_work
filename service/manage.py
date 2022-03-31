import click
import logging
import sys
from create_db import Base, engine
from sqlalchemy.orm import sessionmaker
from seed import seed_Heroes, seed_Hero_motos, seed_Hero_stories, seed_Battles
from ddl_funcs import add_hero, add_hero_moto, add_hero_story, run_battle, delete_hero

class AlchemyFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return record.pathname.find('sqlalchemy/engine') == -1


class DrawFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return record.message.find('Result: Draw') == -1


@click.group()
@click.pass_context
def cli(ctx):
    level = logging.DEBUG
    logging.basicConfig(
        level=level,
        filename="debug.txt",
        filemode="a+"
    )
    logging.getLogger("debug_logger").setLevel(level)

    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    console_formatter = logging.Formatter("%(filename)s.%(funcName)s, %(levelname)s: %(message)s")
    console.setFormatter(console_formatter)
    logging.getLogger("").addHandler(console)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.addFilter(AlchemyFilter())
    logging.getLogger("").addHandler(stream_handler)

    draw_handler = logging.StreamHandler(sys.stdout)
    draw_handler.addFilter(DrawFilter())
    logging.getLogger("debug_logger").addHandler(draw_handler)

    another_file_handler = logging.FileHandler("not_debug.txt", mode="a+")
    another_file_handler.setLevel(logging.INFO)
    another_file_formatter = logging.Formatter("%(asctime)s.%(msecs)4d: %(message)s")
    another_file_handler.setFormatter(another_file_formatter)
    another_file_logger = logging.getLogger("another_file")
    another_file_logger.addHandler(another_file_handler)
    ctx.obj["another_file_logger"] = another_file_logger


@cli.command("create_db")
@click.pass_context
def create_db(ctx):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    ctx.obj["another_file_logger"].info("Base was created")


@cli.command("seed_db")
@click.pass_context
def seed_db(ctx):
    Session = sessionmaker(bind=engine)
    seed_Heroes(Session)
    ctx.obj["another_file_logger"].info("Seeded heroes was added to database")
    seed_Hero_motos(Session)
    ctx.obj["another_file_logger"].info("Seeded motos was added to database")
    seed_Hero_stories(Session)
    ctx.obj["another_file_logger"].info("Seeded stories was added to database")
    seed_Battles(Session)
    ctx.obj["another_file_logger"].info("Seeded battles was added to database")
    


@cli.command("add_hero")
@click.pass_context
def add_db_hero(ctx):
    Session = sessionmaker(bind=engine)
    add_hero(Session)
    ctx.obj["another_file_logger"].info("Hero was added")


@cli.command("add_moto")
@click.pass_context
def add_db_hero_moto(ctx):
    Session = sessionmaker(bind=engine)
    add_hero_moto(Session)
    ctx.obj["another_file_logger"].info("Moto was added")


@cli.command("add_story")
@click.pass_context
def add_db_hero_story(ctx):
    Session = sessionmaker(bind=engine)
    add_hero_story(Session)
    ctx.obj["another_file_logger"].info("Story was added")


@cli.command("run_battle")
@click.pass_context
def add_db_battle(ctx):
    Session = sessionmaker(bind=engine)
    run_battle(Session)
    ctx.obj["another_file_logger"].info("Battle was added")


@cli.command("delete_hero")
@click.pass_context
def delete_db_hero(ctx):
    Session = sessionmaker(bind=engine)
    delete_hero(Session)
    ctx.obj["another_file_logger"].info("Hero was deleted")


if __name__ == "__main__":
    cli(obj={})