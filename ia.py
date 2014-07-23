class AI():
    def __init__(self, parent):
        self.settings = parent.settings
        self.field = parent.field
    
    def Move(self):
        return self.__randomMove()
    def __randomMove(self):
        x, y = randint(0, self.settings.m-1), randint(0, self.settings.n-1)
        while not self.field.move(self.settings.AIplayer, x, y):
            x, y = randint(0, self.settings.m-1), randint(0, self.settings.n-1)
        else:
            return True
        
        
    def defineBorders(lista, border, m, n):
        """ Macro-Function: resizes the table eliminating empty areas for ia's faster computing. 
            Looks like the hell of algorithms and is not really necessary for non-huge fields """

        hold = 0
        for i in range(m-border):
            for j in range(n-border):
                if lista[i][j] == 1:
                    hold = border
                elif lista[i][j+border] == 1:
                    hold = border
                elif lista[i+border][j] == 1:
                    hold = border
                elif hold > 0:
                    hold -= 1
                else:
                    lista[i][j] = -1
        # Finish analysing the right low  end
        for i in range(m-border, m):
            for j in range(n-border, n):
                if lista[i][j] == 1:
                    hold = border
                if hold > 0:
                    hold -= 1
                else:
                    lista[i][j] = -1
    
        # Eliminate useless lines.. not if in the middle but only on borders!

        # These don't really seem to be efficient... but
        linesToRemove = []
        rowsToRemove = []
        # Top-down
        for i in range(m):
            if lista[i].count(-1) == n:
                linesToRemove.append(i)
                break
        # Reverse
        for i in range(m)[::-1]:            # Reversed range with list properties
            if lista[i].count(-1) == n:
                linesToRemove.append(i)
                break

        # Eliminate useless columns
        # Left-right
        for j in range(n):
            for i in range(m):
                if lista[i][j] != -1:
                    break
            else:
                rowsToRemove.append(j)
                continue
            break
    
        # Reverse
        for j in range(n)[::-1]:
            for i in range(m):
                if lista[i][j] != -1:
                    break
            else:
                rowsToRemove.append(j)
                continue
            break
    
        # Removing
    
        for line in reversed(linesToRemove):        # Start at highest index to avoid IndexError
            del lista[line]
            m -= 1
        for i in range(m):
            for j in range(n)[::-1]:
                if j in rowsToRemove:
                    del lista[i][j]
        
            
    
    
        return lista
    
    
    
    def printList(lista):
        for i in range(len(lista)):
            print lista[i]
        print '-------'
    
    
    if __name__ == '__main__':
        lista = [[0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,1,0],
                 [0,0,0,0,0,0,0,1,1,0],
                 [0,0,0,0,0,0,0,0,0,0]]
    
        printList(lista)
        result = defineBorders(lista, 2, 4, 10)
        printList(result)

