import numpy as np

class team():
    points=0
    def __init__(self,name,S):
        self.name=name
        self.S=S
    def change_points(self,n):
        self.points+=n
    def play(self,team2:team):
        if np.random.normal(loc=0)
class league():
    def __init__(self,L):
        self.list=L
    def standings(self):
        points=np.array(t.points for t in self.list)
        sorted_index=np.argsort(points)
        return [self.list[i] for i in sorted_index]
