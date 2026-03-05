class Player:
    def __init__(self, str, agi, hp, weapon):
        self.str = str
        self.agi = agi
        self.hp = hp
        self.weapon = weapon
        self.armor = 'leather'

    def show_info(self):
        info = f'СИЛА: {self.str}, ЛОВКОСТЬ: {self.agi}, ЗДОРОВЬЕ: {self.hp}, ОРУЖИЕ: {self.weapon}, БРОНЯ: {self.armor}'
