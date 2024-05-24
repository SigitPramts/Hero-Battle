from Enemy import *
import random

class Orge(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Orge', 
                         health_points=health_points, 
                         attack_damage=attack_damage)
    
    def talk(self):
        print('Orge is slamming hands all around!')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print('Orge get angry and increases attack by 4!')