#!/usr/bin/env python
# from __future__ import print_function
import random


def rand_dead_blocks(self, num_dead_blocks=1, coeff_surround=-0.2, square_to_modify=2, fade=True):
    maxM = self.settings.m-1
    maxN = self.settings.n-1
    maxIteration = 50000
    # print(maxM, maxN)
    randGen = lambda maxi, mini = 0: random.randint(mini, maxi)
    print "\n-- New Randomblocks generation|"
    def choose_square(self, coeff, square_to_modify, usable_coords, Fade=fade):
        # i = 0
        while True:
            # x = randGen(maxM)
            # y = randGen(maxN)
            x, y = random.choice(usable_coords)
            if self.field[y][x] == 0 and self.values_per_square[(x, y)] > randGen(100)/100.0:
                # print("({},{}) {}".format(x+1, y+1, self.values_per_square[(x, y)]))
                self.field[y][x] = -1
                usable_coords.remove((x, y))
                mod_surround(self, y, x, coeff, square_to_modify, Fade)
                self.values_per_square[(x, y)] = 0
                return
            if i == maxIteration:
                print "Exception raised; last x, y = {}\n".format((x,y))
                raise Exception
            else:
                i += 1

    def mod_matrix(self, value_to_set=1, maxm=maxM+1, maxn=maxN+1, minM=0, minN=0):
        for x in range(0 if minN < 0 else minN, maxN+1 if maxn > maxN+1 else maxn):
            for y in range(0 if minM < 0 else minM, maxM+1 if maxm > maxM+1 else maxm):
                if value_to_set == 1:
                    self.values_per_square[(x, y)] = value_to_set
                else:
                    self.values_per_square[(x, y)] += value_to_set

    def mod_surround(self, X, Y, coeff, square_to_modify, fade):
        for x in range(square_to_modify+1, 1, -1):
            mod_matrix(self, coeff/float(square_to_modify if fade else 1), X+x, Y+x, X-x+1, Y-x+1)
    def rescue(self):
        i = 1
        x,y = (randGen(self.settings.m-1), randGen(self.settings.n-1))
        while True:
            if self.field[x][y] == 0:
                print "Rescued..."
                self.field[x][y] = -1
                break
            elif i==maxIteration:
                print "------> DEATH <------"
                i = 0
                break
            else: i+=1
                
        
    self.values_per_square = {}
    mod_matrix(self)
    usable_coords = self.values_per_square.keys()

    for square in range(0, num_dead_blocks):
        try:
            choose_square(self, coeff_surround, square_to_modify, usable_coords)
        except Exception:
            rescue(self)
        
        

    #     field=[self.values_per_square[x] for x in sorted(self.values_per_square.iterkeys())]
    #     i=1
    #     for el in field:
    #         print(str(el).center(7, " "), end= "")
    #         if i%(maxM+1) == 0:
    #             i=0
    #             print("")
    #         i+=1
    # for el in self.field:
    #     print(el)
