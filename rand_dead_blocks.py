#!/usr/bin/env python

import random
def rand_dead_blocks(self,num_dead_blocks=1,coeff_surround=-0.5,square_to_modify=2):
    maxM=self.settings.m-1
    maxN=self.settings.n-1
    randGen=lambda maxi,mini = 0: random.randint(mini,maxi)
    self.values_per_square = {}
    def mod_matrix(self,value_to_set=1,maxm=maxM+2,maxn=maxN+2,minM=0,minN=0):
        for x in range(0, maxm):
            for y in range(0,maxn):
                if self.values_per_square == 1:
                    self.values_per_square[(x,y)]=value_to_set
                else:
                    try:
                        self.values_per_square[(x,y)]+=value_to_set
                    except KeyError:
                        pass
    mod_matrix()
    def mod_surround(self, X, Y, coeff, square_to_modify):
        mod_matrix(value_to_set=coeff,maxm=X+square_to_modify,maxn=Y+square_to_modify, 
                    minM=X-square_to_modify,minN=Y-square_to_modify)
    def choose_square(self,coeff,square_to_modify):
        while True:
            x = randGen(maxM)
            y = randGen(maxN)
            if self.field[x][y] == 0 and self.values_per_square[(x,y)] >= ranGen(100)/100.0:
                self.field[x][y] = -1
                mod_surround(x,y,coeff,square_to_modify)
                exit

    for square in range(0,num_dead_blocks+1):
        choose_square(coeff_surround,square_to_modify)


class Settings():
    def __init__(self):
        self.m=100
        self.n=100
class Test():
    def __init__(self):
        self.settings=Settings()
    def randgen(self):
        return rand_dead_blocks(self,10)
test=Test()
print test.randgen()
