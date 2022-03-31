# Database_work
Noticement: filter logger doesn't work
## Topic. Bakugan
The database contains **four** tables:

### Heroes
id - Serial, **Primary key** <br> 
side = ENUM(Side) - hero's side. Side can be 'Earth', 'Death world' <br>
name - String(40), unique, NOT NULL - the hero's name <br>
space = ENUM(Space) - hero's space. Space can be 'Fire', 'Terra', 'Aquas', 'Darkus', 'Haos', 'Ventus' <br>
force = Integer, force > 0 - hero's force. Influences on results of battles <br>

### Hero_motos
id - Serial, **Primary key** <br>
hero_id - Integer, ForeignKey(Heroes.id) <br>
moto_id - Integer - the number of hero's moto <br>
moto - String(100) - hero's moto <br>

### Hero_stories
id - Serial, **Primary key** <br>
hero_id - Integer, ForeignKey(Heroes.id) <br>
story - String(1000) - hero's story <br>

### Battles
id - Serial, **Primary key** <br>
hero_1_id - Integer, ForeignKey(Heroes.id) <br>
hero_1_moto_id - Integer, ForeignKey(Hero_motos.id) <br>
hero_2_id - Integer, ForeignKey(Heroes.id) <br>
hero_2_moto_id - Integer, ForeignKey(Hero_motos.id) <br>
winner - Integer - **Draw = 0**, **Hero 1 win = 1**, **Hero 2 win = 2** <br><br>

# Commands
To run a container with development mode
```Linux Kernel Module
docker-compose up -d --build
```
To run a container with production mode
```Linux Kernel Module
docker-compose -f docker-compose.prod.yml up -d --build
```
To shut down a container
```Linux Kernel Module
docker-compose down -v
```
## For local machine 
To create the database
```Linux Kernel Module
docker-compose exec bakugan python manage.py create_db
```
To fill the database with some seed data
```Linux Kernel Module
docker-compose exec bakugan python manage.py seed_db
```
#### INTERACTIVE COMMANDS
To add a hero into the database
```Linux Kernel Module
docker-compose exec bakugan python manage.py add_hero
```
To add a moto into the database
```Linux Kernel Module
docker-compose exec bakugan python manage.py add_moto
```
To add a story into the database
```Linux Kernel Module
docker-compose exec bakugan python manage.py add_story
```
To run a battle and to add its result into the database
```Linux Kernel Module
docker-compose exec bakugan python manage.py run_battle
```
To delete a hero from the database
```Linux Kernel Module
docker-compose exec bakugan python manage.py delete_hero
```
## For cli in docker
To create the database
```Linux Kernel Module
python manage.py create_db
```
To fill the database with some seed data
```Linux Kernel Module
python manage.py seed_db
```
#### INTERACTIVE COMMANDS
To add a hero into the database
```Linux Kernel Module
python manage.py add_hero
```
To add a moto into the database
```Linux Kernel Module
python manage.py add_moto
```
To add a story into the database
```Linux Kernel Module
python manage.py add_story
```
To run a battle and to add its result into the database
```Linux Kernel Module
python manage.py run_battle
```
To delete a hero from the database
```Linux Kernel Module
python manage.py delete_hero
```
