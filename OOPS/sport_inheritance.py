# inheritance help us to reduce code duplication
# inheritance help us to build a relationship between classes
# inheritance help us to build a hierarchy of classes

import datetime

class Player:
    def __init__(self, fname,lname,team,birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        
    def get_age(self):
        return datetime.datetime.now().year - self.birth_year
    
    
class CricketPlayer(Player):
    def __init__(self, fname,lname,team,birth_year):
        Player.__init__(self,fname,lname,birth_year)
        self.team = team
        self.scores = []
        
    def add_score(self,score):
        self.scores.append(score)
        
    def get_average_score(self):
        return sum(self.scores) / len(self.scores)
    
class TennisPlayer(Player):
    def __init__(self, fname,lname,birth_year,gwinner):
        Player.__init__(self,fname,lname,birth_year)
        self.grand_slam_winner = gwinner
        self.aces = []
        
    def get_average_aces_per_match(self):
        return sum(self.aces) / len(self.aces)
    

virat = CricketPlayer('Virat','Kohli','India',1988)
virat.add_score(45)
virat.add_score(78)
virat.add_score(12)
virat.add_score(8)

print(f'Age of Virat: {virat.get_age()}')
print(f'Average score of Virat: {virat.get_average_score()}')

roger = TennisPlayer('Roger','Federer',1981,20)
roger.aces.append(10)
roger.aces.append(15)
roger.aces.append(20)
roger.aces.append(25)

print(f'Age of Roger: {roger.get_age()}')
print(f'Average aces of Roger: {roger.get_average_aces_per_match()}')


