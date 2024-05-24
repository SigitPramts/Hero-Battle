class Enemy:

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f'Aku {self.__type_of_enemy}. Bersiaplah untuk bertempur!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} mendekat kearahmu.')

    def attack(self):
        print(f'{self.__type_of_enemy} menyerang untuk {self.attack_damage} kerusakan.')

    def special_attack(self):
        print('Enemy has no special attack.')

    def get_type_of_enemy(self):
        return self.__type_of_enemy