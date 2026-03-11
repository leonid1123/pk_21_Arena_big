import sqlite3
import os

from player import Player
from db_handler import DB_handler

my_db = DB_handler()
inp = input('Добавить оружие? (Д)а')
if inp == 'Д':
    my_db.add_weapon()
    my_db.get_weapon()
inp = input('Добавить броню? (Д)а')
if inp == 'Д':
    my_db.add_armour()
    my_db.get_armour()

player = Player(1,1,1,None)
os.system('cls')
print('Добро пожаловать в игру КРОВАВАЯ АРЕНА СТРАШНОЙ СМЕРТИ')
print('В начале все характеристики равны 1 и у героя есть КОЖАНАЯ броня.')
print('У вас есть 5 очков для распределения.')
print('Можно выбрать оружие на старте: МЕЧ, КОПЬЁ или ТОПОР')
start_pts = 5
while start_pts > 0:
    char_selected = None
    while char_selected not in ["1", "2", "3"]:
        print(f'Осталось распределить {start_pts} ')
        char_selected = input('Какую характеристику вы хотите улучшить? 1-СИЛА,2-ЛОВКОСТЬ,3-ЖИЗНЬ ')
    if char_selected == '1':
        player.str = player.str + 1
    if char_selected == '2':
        player.agi = player.agi + 1
    if char_selected == '3':
        player.hp = player.hp + 1
    start_pts -= 1
    player.show_info()

char_selected = None
while char_selected not in ["1", "2", "3"]:
    char_selected = input('Какое оружие возьмет герой? 1-МЕЧ, 2-КОПЬЁ или 3-ТОПОР')
if char_selected == '1':
    player.weapon = 'МЕЧ'
if char_selected == '2':
    player.weapon = 'КОПЬЁ'
if char_selected == '3':
    player.weapon = 'ТОПОР'
player.show_info()
