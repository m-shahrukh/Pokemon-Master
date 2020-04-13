
typeAdvantages={
    "Fire": ["Grass, Ice"],
    "Water": ["Fire", "Rock"],
    "Grass": ["Water", "Rock"],
    "Ice": ["Grass"],
    "Rock": []
}

class Pokemon:
    def __init__(self, name, level, pokeType, maxHealth, currentHealth, faint=False):
        self.name=name
        self.type=pokeType
        self.level=level 
        self.maxHealth=maxHealth
        self.currentHealth=currentHealth
        self.isFaint=faint

    def knock_out(self):
            self.currentHealth=0
            self.isFaint=True 
            print(f"{self.name} fainted!")
    
    def lose_health(self, damage):
        self.currentHealth-=damage
        print(f"{self.name} now has {self.currentHealth} health!") 
        if self.currentHealth<=0:
            self.knock_out()
    
    def gain_health(self, recovery):
         if recovery+self.currentHealth>=self.maxHealth:
             self.currentHealth=self.maxHealth
         else:
            self.currentHealth+=recovery
         print(f"{self.name} now has {self.currentHealth} health!")
    
    def revive(self):
        self.currentHealth=self.maxHealth/2
        print(f"{self.name} has been revived. It now has {self.currentHealth} health!")
    
    
    def attack(self, enemy):
        #Dealing with Water, Fire, Grass, Ice, and Rock types
        damage=0
        if enemy.type in typeAdvantages[self.type]:
            #do double damage
            damage=self.level*2

        elif self.type in typeAdvantages[enemy.type]:
            #do half damage
            damage=self.level/2
        else:
            #do normal damage
            damage=self.level
        
        print(f"{self.name} attacked {enemy.name} and dealt {damage} damage!")
        enemy.lose_health(damage)
    
    