import sqlite3


class DB_handler:
    def __init__(self):
        self.conn = sqlite3.connect('bloody_death.db')
        self.cur = self.conn.cursor()
        sql_table_1 = '''CREATE TABLE IF NOT EXISTS Weapon(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Base_dmg INTEGER,
        Type TEXT)'''
        self.cur.execute(sql_table_1)
        self.conn.commit()
        sql_table_2 = '''CREATE TABLE IF NOT EXISTS Armour(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Dmg_dec INTEGER,
        Str_req INTEGER)'''
        self.cur.execute(sql_table_2)
        self.conn.commit()

    def get_weapon(self):
        self.cur.execute('SELECT * FROM Weapon')
        ans = self.cur.fetchall()
        for item in ans:
            print(item)

    def get_armour(self):
        self.cur.execute('SELECT * FROM Armour')
        ans = self.cur.fetchall()
        for item in ans:
            print(item)

    def add_weapon(self):
        sql = 'INSERT INTO Weapon(Name, Base_dmg, Type) VALUES(?,?,?)'
        new_values = (
            ('Деревянный меч', 1, "sword"),
            ('Железный меч', 10, "sword"),
            ('Топор лесника', 2, "axe"),
            ('Топор жены лесника', 12, "axe"),
            ('Копье пилигрима', 2, "spear"),
            ('Копье стражника', 11, "spear")
        )
        self.cur.executemany(sql, new_values)
        self.conn.commit()

    def add_armour(self):
        sql = 'INSERT INTO Armour(Name, Dmg_dec, Str_req) VALUES(?,?,?)'
        new_values = (
            ('Кожаная', 10, 0),
            ("Кольчуга", 15, 0),
            ("Полный доспех", 50, 25)
        )
        self.cur.executemany(sql, new_values)
        self.conn.commit()

    def get_selected_weapon_type(self, _type):
        sql = 'SELECT Id FROM Weapon WHERE Type=? ORDER BY Base_dmg ASC'
        self.cur.execute(sql, (_type,))
        ans = self.cur.fetchone()
        selected_weapon_id = ans[0]
        return selected_weapon_id

    def get_selected_armour(self):
        sql = 'SELECT Id FROM Armour ORDER BY Dmg_dec ASC'
        self.cur.execute(sql)
        ans = self.cur.fetchone()
        selected_armour_id = ans[0]
        return selected_armour_id

    def get_weapon_by_id(self,_id):
        sql = '''SELECT Name, Base_dmg FROM Weapon
        WHERE Id=?'''
        self.cur.execute(sql, (_id,))
        ans = self.cur.fetchone()
        return ans

    def get_armor_by_id(self,_id):
        sql = '''SELECT Name, Dmg_dec FROM Armour
        WHERE Id=?'''
        self.cur.execute(sql,(_id,))
        ans = self.cur.fetchone()
        return ans

