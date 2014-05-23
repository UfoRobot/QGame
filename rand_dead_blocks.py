#!/usr/bin/env python

import random
def rand_dead_blocks(self,num_dead_blocks,coeff_surround=0.5):
    maxm=self.settings.m-1
    maxn=self.settings.n-1
    randm=lambda max,min=0: random.randint(min,max)
    randn=random.randint(0,maxn)
    return randm(maxm)
    # self.field[random.randint(0, self.settings.m-1)][random.randint(0, self.settings.n-1)]

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
