# pokemann.py
#
# By Ian Thompson and Morgan Theys

import random

class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file

        self.current_health = health

    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                    
        return result
    
    def execute_move(self, move, target):
        available = self.get_available_moves()
        
        if self.fainted:
            print("Error: " + self.name + " is fainted!")
        elif move not in available:
            print("Error: " + move.name + " is not available.")
        else:
            r = random.randint(1, 100)

            if r <= move.accuracy:
                damage = move.get_damage(self, target)
                target.apply_damage(damage)
                print(move.name + " hits " + target.name + " for " + str(damage) + ".")
            else:
                print(move.name + "missed!")

            move.remaining_power -= 1

    def take_damage(self, amount):
        self.current_health -= amount
        
        if self.current_health <= 0:
            self.faint()

    def faint(self):
        self.current_health = 0
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        """
        Raises current_health by amount but not to more than the base health.
        """
        self.current_health += amount

        if self.current_health > self.health:
            self.current_health = self.health

        self.fainted = False


        print(self.name + " is healed and has " + str(self.current_health) + " health!")
        
    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                  
        return result
                  
    def get_move(self):
        """
        This might only be used by computer controlled Pokemann. Perhaps
        'better' Pokemann could be smarter about the random move they choose.
        """
        available = self.get_available_moves()
        return random.choice(available)

    def draw(self):
        pass


class Move:
    STRONG = 2.0
    NORMAL = 1.0
    WEAK = 0.5
        
    effectiveness = {
            ('student' ,'administrator'): STRONG,
            ('student' ,'student'): NORMAL,
            ('student', 'teacher'): WEAK,
            ('teacher', 'student'): STRONG,
            ('teacher' ,'teacher'): NORMAL,
            ('teacher' ,'administrator'): WEAK,
            ('administrator' ,'teacher'): STRONG,
            ('administrator', 'administrator'): NORMAL,
            ('administrator', 'student'): WEAK
          }
                 
    def __init__(self, name, kind, powerpoint, power, accuracy):
        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = power

    def get_damage(self, attacker, target):

        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]

        return int(p * a / d * e)

    def restore(self, amount):
        self.

                      
class Player:

    def __init__(self, characters):
        pass

    def fight(self, target):
        '''
        1. Select a move (from available of character[0])
        2. target_move = target.get_move()
        3. check speed for 1st attack
        4. one attacks two
            self.execute_move(move, target)
        5. if two alive, two attacks 1
            target.execute_move(move, self)
        '''
        pass

    def catch(self, target):
        pass
    
    def draw(self):
        pass
                  
                  
class Game:

    def __init__():
        pass

    def loop(self):
        # get input

        # do logic stuff
        if player.intersects(pokemann):
            player.fight(pokemann)

        if player.intersects(potion):
            # pick character to heal
            pass

        # draw stuff


if __name__ == '__main__':

    # Make some moves
    homework = Move("Homework", "teacher", 80, 10, 100)
    pop_quiz = Move("Pop quiz", "teacher", 20, 60, 45)
    lecture = Move("Lecture", "teacher", 50, 30, 60)
    teacher_strike = Move("Teacher Strike", "teacher", 20, 60, 45)
    complaining_about_freezer_space = Move("Complaining about freezer space", "teacher", 80, 10, 100)
    phone_out = Move("Phone out During Lesson", "student", 80, 10, 100)
    no_homework = Move("No Homework", "student", 50, 30, 60)
    talking_back = Move("Talking Back", "student", 20, 60, 45)
    complaing_problems = Move("Complaining About Social Life Problems", "student", 50, 30, 60)
    ask_for_id = Move("Ask for ID", "admin", 60, 10, 100)
    call_parents = Move("Call Parents", "admin", 40, 40, 70)
    expulsion = Move("Expulsion", "admin", 10, 80, 35)
    fire_staff_member = Move("Fire Staff Member", "admin", 10, 80, 35)
    restrict_lunchtime = Move("Restrict Lunchtime", "admin", 40, 40, 70)

    # Create some Pokemann(s)
    rooksabee = Pokemann("rooksabee", "teacher", 30, 20, 50, 30, [homework, pop_quiz, teacher_strike], "coopasaur.png")
    criderbat = Pokemann("criderbat", "teacher", 30, 20, 50, 30, [complaining_about_freezer_space, teacher_strike, lecture], "mayfieldarow.png")
    grantizard = Pokemann("grantizard", "teacher", 30, 20, 50, 30, [homework, teacher_strike, lecture], "andrewag.png")
    coopazoid = Pokemann("coopazoid", "teacher", 30, 20, 50, 30, [teacher_strike, homework, lecture], "andrewag.png")
    mayflower = Pokemann("mayflower", "admin", 30, 20, 50, 30, [ask_for_id, call_parents, call_parents], "andrewag.png")
    bishlypuff = Pokemann("bishlypuff", "admin", 30, 20, 50, 30, [ask_for_id, call_parents, call_parents], "andrewag.png")
    sartinoid = Pokemann("sartinoid", "admin", 30, 20, 50, 30, [ask_for_id, call_parents, call_parents], "andrewag.png")
    fresheon = Pokemann("fresheon", "student", 30, 20, 50, 30, [no_homework, talking_back, complaing_problems], "andrewag.png")
    seniatar = Pokemann("seniatar", "student", 30, 20, 50, 30, [no_homework, talking_back, complaing_problems], "andrewag.png")
    
