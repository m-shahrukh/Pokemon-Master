
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

    def knockOut(self):
            self.currentHealth=0
            self.isFaint=True 
            print(f"{self.name} fainted!")
    
    def loseHealth(self, damage):
        self.currentHealth-=damage
        print(f"{self.name} now has {self.currentHealth} health!") 
        if self.currentHealth<=0:
            self.knockOut()
    
    def gainHealth(self, recovery):
         if recovery+self.currentHealth>=self.maxHealth:
             self.currentHealth=self.maxHealth
         else:
            self.currentHealth+=recovery
         print(f"{self.name} now has {self.currentHealth} health!")
    
    def revive(self):
        self.currentHealth=self.maxHealth/2
        self.isFaint=False
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
        enemy.loseHealth(damage)
    
    def __repr__(self):
        return f"{self.name}"

class Trainer:
    def __init__(self,name,numPotions,currPoke, pokeTeam=None):
        self.name=name 
        self.numPotions=numPotions
        self.currPoke=currPoke
        if pokeTeam==None:
            self.pokeTeam=[self.currPoke]
        elif len(pokeTeam)>6:
            print("You cannot have more than 6 pokemon! Only the first 6 in the team will be selected")
            self.pokeTeam=pokeTeam[:6]
        else:
            self.pokeTeam=pokeTeam
        
    def usePotion(self):
        if self.numPotions>0:
            self.pokeTeam[self.currPoke].gainHealth(20)
            print(f"{self.name} used a Potion!")
        else:
            print(f"{self.name} doesn't have any potions left!")
    
    def attackOther(self, otherTrainer):
        self.pokeTeam[self.currPoke].attack(otherTrainer.pokeTeam[otherTrainer.currPoke])

    def switchPoke(self, pokeToSwitch):
        if pokeToSwitch.isFaint:
            print(f"{pokeToSwitch} has fainted, can't switch to it.")
        elif pokeToSwitch not in self.pokeTeam:
            print(f"{pokeToSwitch} is not in your team!")
        else:
            self.currPoke= self.pokeTeam.index(pokeToSwitch)
        