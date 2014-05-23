#!/usr/bin/env python

import random
def rand_dead_blocks(self,num_dead_blocks=1,coeff_surround=-0.2,square_to_modify=2):
    maxM=self.settings.m-1
    maxN=self.settings.n-1
    randGen=lambda maxi,mini = 0: random.randint(mini,maxi)
    def choose_square(self,coeff,square_to_modify):
        while True:
            x = randGen(maxM)
            y = randGen(maxN)
            if self.field[x][y] == 0 and self.values_per_square[(x,y)] >= ranGen(100)/100.0:
                self.field[x][y] = -1
                mod_surround(x,y,coeff,square_to_modify)
                exit
    def mod_matrix(self,value_to_set=1,maxm=maxM+2,maxn=maxN+2,minM=0,minN=0):
        if maxm>self.settings.m+1:
            maxm=self.settings.m+1
        if maxn>self.settings.n+1:
            maxn=self.settings.n+1
        if minN<0:
            minN=0
        if minM<0:
            minM=0
        for x in range(minM, maxm):
            for y in range(minN,maxn):
                if self.values_per_square[(x,y)]== 1:
                    self.values_per_square[(x,y)]=value_to_set
                else:
                    self.values_per_square[(x,y)]+=value_to_set
    def mod_surround(self, X, Y, coeff, square_to_modify):
        mod_matrix(value_to_set = coeff , maxm = X + square_to_modify,maxn=Y+square_to_modify, 
                    minM=X-square_to_modify,minN=Y-square_to_modify)

    self.values_per_square = {}
    mod_matrix(self)
    
    for square in range(0,num_dead_blocks+1):
        choose_square(self,coeff_surround,square_to_modify)


class Settings():
    def __init__(self):
        self.m=100
        self.n=100
class Test():
    def __init__(self):
        self.settings=Settings()
    def randgen(self):
        return rand_dead_blocks(10)
test=Test()
print test.randgen()
