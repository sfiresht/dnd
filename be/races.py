races = {
    'orc': { 'strength': 150, 'health': 200, 'dexterity': 50, 'wisdom': 10 },
    'elf': { 'strength': 50, 'health': 150, 'dexterity': 150, 'wisdom': 100 },
    'human': { 'strength': 100, 'health': 100, 'dexterity': 100, 'wisdom': 75 }
}


class race():
    def __init__(self, name):
        race_attributes = races[name]
        self.name = name
        self.strength = race_attributes['strength']
        self.health = race_attributes['strength']
        self.dexterity = race_attributes['strength']
        self.wisdom = race_attributes['strength']

    #define what is to be printed if we just print the object name
    def __str__(self):
        return "race: {}, strength {}, health {}, dex {}, wisdom {}".format(self.name, self.strength, self.health, self.dexterity,  self.wisdom )
        
    # def orc():
    #     #base stats
    #     strength = 100
    #     health = 200
    #     dexterity = 50
    #     wisdom = 10
        
    # def elf():
    #     #base stats
    #     strength = 50
    #     health = 150
    #     dexterity = 150
    #     wisdom = 100