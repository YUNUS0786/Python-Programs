from abc import ABC,abstractmethod
class Player(ABC):
    @abstractmethod
    def play(self):
        pass
class CricketPlayer(Player):
        def play(self):
            print("Cricket Players play cricket")

class FootballPlayer(Player):
        def play(self):
            print("FootBall Players play cricket")
        
class TennisPlayer(Player):
        def play(self):
            print("Tennis Players play cricket")
c=CricketPlayer()
c.play()
f=FootballPlayer()
f.play()
t=TennisPlayer()
t.play()
         
                  
