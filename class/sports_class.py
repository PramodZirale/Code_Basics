import datetime

class CricketPalyer:
    def __init__(self, fname,lname,team,birth_year):
        self.first_name = fname
        self.last_name = lname
        self.team = team
        self.birth_year = birth_year
        self.scores = []
        
    def get_age(self):
            return datetime.datetime.now().year - self.birth_year 
        
    def get_score_sum(self):
            return sum(self.scores)
        
    def get_avg_score(self):
            return self.get_score_sum() / len(self.scores) 
        
    def __lt__ (self, other):
        return self.get_score_sum() < other.get_score_sum()
    
    def __eq__ (self, other):
        return self.get_score_sum() == other.get_score_sum()
    
    def __gt__ (self, other):
        return self.get_score_sum() > other.get_score_sum()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.team} {self.birth_year}'
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.team} {self.birth_year}'
    
    def __add__(self, other):
        return self.get_score_sum() + other.get_score_sum()
    
    def __sub__(self, other):
        return self.get_score_sum() - other.get_score_sum()
    
    def __mul__(self, other):
        return self.get_score_sum() * other.get_score_sum()
    
    def __truediv__(self, other):
        return self.get_score_sum() / other.get_score_sum()
    
    def __floordiv__(self, other):
        return self.get_score_sum() // other.get_score_sum()
    
    def __mod__(self, other):
        return self.get_score_sum() % other.get_score_sum()
    
    def __pow__(self, other):
        return self.get_score_sum() ** other.get_score_sum()
    
    def __and__(self, other):
        return self.get_score_sum() & other.get_score_sum()
    
    def __or__(self, other):
        return self.get_score_sum() | other.get_score_sum()
        
        
        
virat = CricketPalyer('Virat','Kohli','RCB',1988)
print(virat.first_name)
print(virat.last_name)
print(virat.team)
print(virat.birth_year)
print(virat.scores)
virat.scores.append(100)
virat.scores.append(78)
virat.scores.append(12)
virat.scores.append(8)
print(f'Virat scores: {virat.scores}')
print(f'Virat age: {virat.get_age()}')
print(f'Virat total score: {virat.get_score_sum()}')

yuvraj = CricketPalyer('Yuvraj','Singh','Punjab',1981) 
print(yuvraj.first_name)
print(yuvraj.last_name)
print(yuvraj.team)
print(yuvraj.birth_year)
print(yuvraj.scores)
yuvraj.scores.append(45)
yuvraj.scores.append(78)
yuvraj.scores.append(12)
yuvraj.scores.append(8)
print(f'Yuvraj scores: {yuvraj.scores}')
print(f'Yuvraj age: {yuvraj.get_age()}')
print(f'Yuvraj total score: {yuvraj.get_score_sum()}')

 
#Operator overloading
print(virat + yuvraj)
print(virat - yuvraj)
print(virat * yuvraj)
print(virat / yuvraj)
print(virat // yuvraj)
print(virat % yuvraj)
print(virat<yuvraj)
print(virat>yuvraj)


