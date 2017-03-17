# pokemann.py
#
# By Ian Thompson and Morgan Theys

import random

class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, catch_rate, health, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.catch_rate = catch_rate
        self.health = health
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file
        self.fainted = False

        self.current_health = health

    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                #print(m.name)
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
                damage = move.calculate_damage(self, target)
                print(self.name + " hits " + target.name + " with " + move.name  + " for " + str(damage) + ".")
                target.take_damage(damage)
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

    def restore(self):
        """
        Restores all health and resets powerpoint for all moves.
        """
        self.current_health = self.health

        for m in self.moves:
            m.restore()
        

    
class Move:
    STRONG = 2.0
    NORMAL = 1.0
    WEAK = 0.5
        
    effectiveness = {
            ('student' ,'admin'): STRONG,
            ('student' ,'student'): NORMAL,
            ('student', 'teacher'): WEAK,
            ('teacher', 'student'): STRONG,
            ('teacher' ,'teacher'): NORMAL,
            ('teacher' ,'admin'): WEAK,
            ('admin' ,'teacher'): STRONG,
            ('admin', 'admin'): NORMAL,
            ('admin', 'student'): WEAK
          }
                 
    def __init__(self, name, kind, powerpoint, power, accuracy):
        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = power

    def calculate_damage(self, attacker, target):

        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]

        return int(p * a / d * e)

    def restore(self):
        """
        Resets remaing_power to starting powerpoint.
        """

        self.remaining_power = self.powerpoint
        
        

                      
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
                  

class Character:
    
    def __init__(self, name, pokemann, image):
        self.name = name
        self.pokemann = pokemann
        self.image = image

    def get_available_pokemann(self):
        """
        Returns a list of all unfainted Pokemann belonging to a character.
        """

        
        result = []

        for p in self.pokemann:
            if p.current_health > 0:
                result.append(p)

        return result
    
    def get_first_pokemann(self):
        """
        Returns the first [0] unfainted character in the pokemann list.
        """
        pass
    
    def set_first_pokemann(self, swap_pos):
        """
        Moves pokemann to first position [0] in the pokemann list by exchanging it with
        pokemann located at swap_pos.
        """
        pass
    
    def draw(self):
        pass

    def restore(self):
        for p in self.pokemann:
            p.restore()
    def get_active_pokemann(self):
        """
        Returns the first unfainted character in the pokemann list. If all pokemann
        are fainted, return None.
        """
        available = self.get_available_pokemann()

        if len(available) > 0:
            return available[0]
        else:
            return None            
                
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


class Player(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)

        self.computer = []
        self.computer = []
        self.pokeballs = 23456789034567789898789876545678987654

    def catch(self, target):
        """
        Can only be applied to a wild pokemann. Determine a catch by generating a random
        value and comparing it to the catch_rate. If a catch is successful, append the
        target to the player's pokemann list. However, if the pokemann list already
        contains 6 pokemann, add the caught target to the players computer instead.
        Pokemann sent to the computer will be fully restored, but other caught pokemann
        will remain at the strength they were caught. Decrease the player's pokeball
        count by 1 regardless of success.
        Return True if the catch is successful and False otherwise.
        """

        r = random.randint(1,100)

        if self.pokeballs != 0:
            self.pokeballs -= 1
            if r <= target.catch_rate:
                if len(self.pokemann) >=6:
                    self.collection.append(target)
                    for n in self.collection:
                        n.restore()
                    print("Computer caught " + target.name + ".")
                else:
                    self.pokemann.append(target)
                    print("You caught " + target.name + ".")
            else:
                print("It got away")
        else:
            print("No Pokeballs Remaining")

    def run(self, target):
        """
        Can only be applied in the presence of a wild pokemann. Success is determined by
        comparing speeds of the player's active pokemann and the wild pokemann. Incoroporate
        randomness so that speed is not the only factor determining success.
        Return True if the escape is successful and False otherwise.
        """

        r = random.randint(1,100)
        s = random.randint(1,20)
        runners = self.get_active_pokemann()

        if runners.speed + r > target.speed + s:
            print("you have escaped")
            return True
        else:
            print("Captured")
            return False
    
class NPC(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)
      

class Game:

    def __init__(self):
        pass

    def select_pokemann(self, character):
        """
        1) Generate a menu which shows a numbered list of all characters along with status (health).
        2) Have the player select a character.
        3) Move the selected character to position [0] in the characters list.
        """
        pass

    def select_random_pokemann(self, pokemann):
        """
        Returns a random available move from the pokemann. This will probably only be used
        by computer controlled pokemann.
        """
        available_moves = pokemann.get_available_moves()
        return random.choice(available_moves)
    
    def select_move(self, pokemann):
        """
        1) Generate a menu which shows a numbered list all available moves for a pokemann.
        2) Have the player select a move.
        3) Return the selected move.
        """

        available = pokemann.get_available_moves()
        
        print("Select a move:")
        
        for i, move in enumerate(available):
            print(str(i) + ") " + move.name)

        n = input("Your choice: ")
        n = int(n)
        
        return available[n]

    def select_random_move(self, pokemann):
        """
        Returns a random available move from the pokemann. This will probably only be used
        by computer controlled pokemann.
        """
        pass

    def fight(self, player_pokemann, target_pokemann):
        """
        This controls the logic for a single round in a fight whether in context of a battle
        or with a wild pokemann.
        
        1. Select player_move (use select_move)
        2. Select target_move (use select_random_move)
        3. Compare speeds of player_pokemann and target_pokemann
            If player_pokemann.speed > target_pokemann.speed, set first = player_pokemann,
            second = target_pokemann. Otherwise, set first = target_pokemann, second = player_pokemann
            If speeds are equal, assign first and second randomly.
        4. Call
            first.execute_move(move, second)
        5. If second is still unfainted, call
            second.execute_move(move, first)
        (Once we have an actual game, we'll need to devise a way to remove fainted targets.)
        """
        pass

    def encounter(self, player, target):
        """
        This function controls all logic when encountering a wild pokemann. Options are to
        fight, catch, or ignore.
        Use a loop so that this continues until a pokemann is fainted, caught, or the
        target is ignored.
        """
        pass
    
    def battle(self, player, opponent):
        """
        This function controls all battle logic including decisions to reorder pokemann,
        fight, use potions, and whatever else happens in Pokebattles.
        Use a loop so that this continues until all characters for either the player or
        opponent are fainted.
        """
        pass
    
    def loop(self):
        pass
    
        # get input

        # do logic stuff

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
    rooksabee = Pokemann("rooksabee", "teacher", 30, 20, 50, 10, 30, [homework, pop_quiz, teacher_strike], "coopasaur.png")
    criderbat = Pokemann("criderbat", "teacher", 30, 20, 50, 23, 30, [complaining_about_freezer_space, teacher_strike, lecture], "mayfieldarow.png")
    grantizard = Pokemann("grantizard", "teacher", 30, 20, 50, 60, 30, [homework, teacher_strike, lecture], "andrewag.png")
    coopazoid = Pokemann("coopazoid", "teacher", 30, 20, 50, 20, 30, [teacher_strike, homework, lecture], "andrewag.png")
    mayflower = Pokemann("mayflower", "admin", 30, 20, 50, 50, 30, [ask_for_id, call_parents, call_parents], "andrewag.png")
    bishlypuff = Pokemann("bishlypuff", "admin", 30, 20, 50, 25, 30, [ask_for_id, call_parents, call_parents], "andrewag.png")
    sartinoid = Pokemann("sartinoid", "admin", 30, 20, 50, 32,30, [ask_for_id, call_parents, call_parents], "andrewag.png")
    fresheon = Pokemann("fresheon", "student", 30, 20, 50, 75, 30, [no_homework, talking_back, complaing_problems], "andrewag.png")
    seniatar = Pokemann("seniatar", "student", 30, 20, 50, 14, 30, [no_homework, talking_back, complaing_problems], "andrewag.png")

    # Create Player
    pat = Player("Pat Riotum", [mayflower, criderbat, grantizard, sartinoid], "pat.png")

    # Create Opponents
    rocket = NPC("Team Rocket", [seniatar, fresheon, rooksabee, sartinoid], "rocket.png")
    jessie = NPC("Jessie", [coopazoid, bishlypuff, rooksabee, seniatar], "jessie.png")

    # Create a game
    g = Game()
 
    
