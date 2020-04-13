
typeAdvantages={
    "Fire": ["Grass", "Ice"],
    "Water": ["Fire", "Rock"],
    "Grass": ["Water", "Rock"],
    "Ice": ["Grass"],
    "Rock": []
}

class Pokemon:
    def __init__(self, name, level, pokeType, faint=False):
        self.name=name
        self.type=pokeType
        self.level=level 
        self.maxHealth=level*5
        self.currentHealth=self.maxHealth
        self.isFaint=faint

    def knockOut(self):
            self.currentHealth=0
            self.isFaint=True 
            print(f"{self.name} fainted!")
    
    def loseHealth(self, damage):
         if self.currentHealth-damage<=0:   
            self.knockOut()
         else:
             self.currentHealth-=damage
             print(f"{self.name} now has {self.currentHealth} health!")
    
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

    def printStats(self):
        print(f"Name: {self.name}, Level: {self.level}, Max Health: {self.maxHealth}, Current Health: {self.currentHealth}.")

    
    def __repr__(self):
        return f"{self.name}"

class Trainer:
    def __init__(self,name,numPotions, pokeTeam):
        self.name=name 
        self.numPotions=numPotions
        self.currPoke=0 #index in the list, initially we take the first pokemon
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
        #pokeToSwitch is a name
        pokemon=None
        for x in self.pokeTeam:
            if x.__repr__()==pokeToSwitch:
                pokemon=x
                break
                
        if pokemon==None:
            print(f"{pokeToSwitch} is not in your team!")
        elif pokemon.isFaint:
            print(f"{pokeToSwitch} has fainted, can't switch to it.")
        else:
            self.currPoke= self.pokeTeam.index(pokemon)
            print(f"{self.name} switched to {pokemon}")
        
    def printCurrPoke(self):
        print(f"{self.name}'s Current Active Pokemon: {self.pokeTeam[self.currPoke]}")
####Testing
alleosPoke=[Pokemon("Charizard", 50, "Fire"), Pokemon("Swampert", 50, "Water")]
alleo= Trainer("Alleo", 5, alleosPoke )
garysPoke=[Pokemon("Venasaur", 50, "Grass"), Pokemon("Onyx", 50, "Rock")]
gary= Trainer("Gary",0, garysPoke)

alleo.printCurrPoke()
for poke in alleo.pokeTeam:
    poke.printStats()
for poke in gary.pokeTeam:
    poke.printStats()
alleo.attackOther(gary)
gary.attackOther(alleo)
alleo.attackOther(gary)
gary.attackOther(alleo)
alleo.attackOther(gary)
gary.switchPoke("Onyx")
# for x in garysPoke:
#     if x.__repr__()=="Venasaur":
#         print(x.level)