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

    n = 0
    m = 0


    #
    # Class methods
    #
    
    # init builds up a clear field n x m
    def __init__(self, rows, columns):
        n = rows
        m = columns
        self.field = [] 
        for row in range(n):
            self.field.append([0 for x in range(m)])

    def checkSequence(self, sequence):
        """ Given a sequence returns the element that occurs 4 times
            in a row. If more the first, if none None """

        mayWin = sequence[0]
        count = 0
        for x in sequence:
            if x == mayWin:
                count += 1
            else:
                mayWin = x
                count = 1
            if count == 4 and mayWin != 0:
                return mayWin
        return None

    def checkRows(self, field = None):
        """ Checks for a winner on field's rows. May be passed a different field """
        if field == None:
            field = self.field
        for row in field:
            mayWin = self.checkSequence(row)
            if mayWin != None:
                return mayWin

    def checkColumns(self, field = None):
        if field == None:
            field = self.field
        column = []

        for j in range(len(field[0])):
            for i in range(len(field)):
                column.append(field[i][j])
            print column
            mayWin = self.checkSequence(column)
            if mayWin != None:
                return mayWin
            else:
                column = []
        return None

    def checkBlock(self, field = None):
        if field == None:
            field = self.field
        block = []

        for i in range(len(field)-1):
            for j in range(len(field[0])-1):
                block.append(field[i][j])
                block.append(field[i][j+1])
                block.append(field[i+1][j])
                block.append(field[i+1][j+1])
                print block
                mayWin = self.checkSequence(block)
                if mayWin != None:
                    return mayWin
                block = []
        return None

    def checkWin(self, field = None):
        if field == None:
            field = self.field
        rowWinner = self.checkRows(field)
        if rowWinner != None:
            return rowWinner
        columnWinner = self.checkColumns(field)
        if columnWinner != None:
            return columnWinner
        blockWinner = self.checkColumn(field)
        if blockWinner != None:
            return blockWinner
        return None



if __name__ == "__main__":
    test = QField(4,6)
#    print test.field
    
#    sequenceLine = [0,0,3,3,3,2,2,0,0,0,0,0,0,0,1,1,1,1]
#    print sequenceLine
#    print test.checkSequence(sequenceLine)

    testField = [
            [1,2,2,0,0,1],
            [1,1,0,0,2,1],
            [2,0,2,2,1,1],
            [2,2,1,2,1,1]
            ]
#    print testField
#    print test.checkRows(testField)
    print test.checkBlock(testField)

