class Player:
    def __init__(self, str, agi, hp):
        self.str = str
        self.agi = agi
        self.hp = hp
        self.weapon = None
        self.armor = None

    def show_info(self, _db_handler):
        if self.armor is None and self.weapon is None:
            info = f'''СИЛА: {self.str}, 
            ЛОВКОСТЬ: {self.agi}, 
            ЗДОРОВЬЕ: {self.hp}, 
            ОРУЖИЕ: нет, 
            БРОНЯ: нет'''
        else:
            arm = _db_handler.get_armor_by_id(self.armor)
            wpn = _db_handler.get_weapon_by_id(self.weapon)
            info = f'''СИЛА: {self.str}, 
            ЛОВКОСТЬ: {self.agi}, 
            ЗДОРОВЬЕ: {self.hp}, 
            ОРУЖИЕ: название:{wpn[0]}-базовый урон:{wpn[1]}, 
            БРОНЯ: название:{arm[0]}-поглощение:{arm[1]}%
            '''
        print(info)