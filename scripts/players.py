import pygame

class Player:
    def __init__(self, name,turn):
        self.name=name
        self.money=350
        self.turn=turn
        
        self.score=0
        self.roster=[]
        self.diceVal=0        
    def score_goal():
        self.score+=1
    def add_to_roster(self,athlete):
        self.roster.append(athlete) #fix later
    def assignDiceVal(self,diceval):
        self.diceVal=diceval
    """
    def buy_athlete(self,athname):
        for a in athletes:
            if a.name==athname:
                self.money-=a.price
                self.add_to_roster(a)
    """
    def buy_athlete(self,athlete):
        if self.money>=athlete.price and len(self.roster)<4:
            self.money-=athlete.price
            self.add_to_roster(athlete)
        
            
                
        
        

class Athlete:
    def __init__(self, name, pos, atk, dfns, stm, price):
        self.name=name
        self.pos=pos
        self.atk=atk
        self.dfns=dfns
        self.stm=stm
        self.price=price
    def reduceStm(num):
        self.stm-=num
    bpos_x=0
    bpos_y=0

def make_athlete(name,pos,atk,dfns,stm,price):
    athlete=Athlete(name,pos,atk,dfns,stm,price)
    return athlete

def make_player(name,turn):
    player=Player(name,turn)
    
    return player


players=[]
players.append(make_player('Player 1',True))
players.append(make_player('Player 2',False))

athletes=[]



athletes.append(make_athlete('Messi', 'FW', 10,4,5,120))
athletes.append(make_athlete('Ronaldo', 'FW', 10,3,7,120))


athletes.append(make_athlete('Suarez', 'FW', 9,3,7,100))
athletes.append(make_athlete('Salah', 'FW', 8,5,8,100))

athletes.append(make_athlete('Dybala', 'FW', 8,4,6,80))
athletes.append(make_athlete('De Bruyne', 'MF', 7,6,5,80))
athletes.append(make_athlete('Pogba', 'MF', 7,5,6,80))
athletes.append(make_athlete('Kante', 'MF', 5,8,5,70))
athletes.append(make_athlete('Ramos', 'DF', 3,9,8,80))
athletes.append(make_athlete('Pique', 'DF', 4,8,7,70))
athletes.append(make_athlete('De Gea', 'GK', 2,8,5,80))
athletes.append(make_athlete('Neuer', 'GK', 3,9,3,90))

"""
athletes.append(make_athlete('Kroos', 'MF' '10','5','7'))
athletes.append(make_athlete('Pogba', 'MF' '10','5','7'))
athletes.append(make_athlete('Kante', 'MF' '10','5','7'))
athletes.append(make_athlete('Busquets', 'MF' '10','5','7'))
athletes.append(make_athlete('Ramos', 'DF' '10','5','7'))
athletes.append(make_athlete('Pique', 'DF' '10','5','7'))
athletes.append(make_athlete('Hummels', 'DF' '10','5','7'))
athletes.append(make_athlete('Chiellini', 'DF' '10','5','7'))
athletes.append(make_athlete('Neuer', 'GK' '10','5','7'))
athletes.append(make_athlete('De Gea', 'GK' '10','5','7'))
athletes.append(make_athlete('Courtois', 'GK' '10','5','7'))
"""

        
            
        
        
