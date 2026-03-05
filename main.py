import sqlite3
import os

from player import Player

os.system('cls')
print('Добро пожаловать в игру КРОВАВАЯ АРЕНА СТРАШНОЙ СМЕРТИ')
print('В начале все характеристики равны 1 и у героя есть КОЖАНАЯ броня.')
print('У вас есть 5 очков для распределения.')
print('Можно выбрать оружие на старте: МЕЧ, КОПЬЁ или ТОПОР')
start_pts = 5
while start_pts >= 0:
    char_selected = None
    while char_selected not in ["1", "2", "3"]:
        char_selected = input('Какую характеристику вы хотите улучшить? 1-СИЛА,2-ЛОВКОСТЬ,3-ЖИЗНЬ')
        if char_selected == '1':
            str_rng = range(1, start_pts+1)
            str_add = ''
            while str_add not in str_rng and str_add.isnumeric():
                str_add = input(f'Сколько очков вложить в СИЛУ? Доступно {start_pts} очков')
                str_add = int(str_add)
                start_pts = start_pts - str_add
