from races import race as RACE
import json



class character():
               
        def __init__(self, name = None, race = None , job = None):
            self.name = name
            self.race = race
            self.job = job
            race_vars = RACE(race)
            self.strength = race_vars.strength
            self.wisdom = race_vars.wisdom
            self.health = race_vars.health
            self.dexterity = race_vars.dexterity
            self.desc = self.description()
            self.stats = self.create_char_dic()

        #define what is to be printed if we just print the object name
        def __str__(self):
             return "my name is {}, my race is {}, I have a job as a {}".format(self.name, self.race, self.job)
                        
        def description(self):
            return "char's name is {}, the char's race is {}".format(self.name, self.race, self.job)
        
        def create_char_dic(self):
             char_dic = {
                  "name": self.name,
                  "race": self.race,
                  "job": self.job,
                  "description": self.desc,
                  "strength": self.strength,
                  "wisdom": self.wisdom,
                  "health": self.health,
                  "dexterity": self.dexterity
             }
             return char_dic

        def save_to_db(self):
            db_file = "./chars.txt"
            with open( db_file, "w" ) as file:
                 print('writing to file')
                 file.write(str(self.stats))
               
        def get_character(self, name):
            db_file = "./chars.txt"
            with open( db_file, "r" ) as file:
                 print('reading from file')
                 data = file.read()
                 print(data)
                 jsondata = json.loads(data)
                 print(jsondata)
                 #return jsondata
                 


        #when ready we'll take this from the database by name only  
        #def __init__(self, name):
            #get data from DB and assign to all vars
            # self.name = name
            # self.race = race
            # self.job = job
            # self.strength = strength
            # self.wisdom = wisdom
            # self.health = health


testchar = character('test', 'orc', 'thief')
testchar = character('test1')



#print(testchar.description())
#print(testchar)
#testchar.save_to_db()
     

