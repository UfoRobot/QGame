#
# Imports under here
#

#
# Class definition
#

class QField():
    """ A field for the Q-Game and all methods needed to play """

    #
    # Class members
    #

    #
    # Class methods
    #
    
    # init builds up a clear field n x m
    def __init__(self, rows, columns):
        self.field = [] 
        for row in range(rows):
            self.field.append([0 for x in range(columns)])



if __name__ == "__main__":
    test = QField(5,3)
    print test.field

