def defineBorders(lista, border, m, n):
    hold = 0
    for i in range(m):
        for j in range(n-border):
            if lista[i][j] == 1:
                hold = border
            elif lista[i][j+border] == 1:
                hold = border
            elif hold > 0:
                hold -= 1
            else:
                lista[i][j] = -1
        # Finish analysing the right end
        for j in range(n-border, n):
            if lista[i][j] == 1:
                hold = border
            if hold > 0:
                hold -= 1
            else:
                lista[i][j] = -1

    # Eliminate unusefuls lines.. not if in the middle but only on borders!
    # Theese don't really seem to be efficient... but
    linesToRemove = []
    rowsToRemove = []
    # Top-down
    for i in range(m):
        if lista[i].count(-1) == n:
            linesToRemove.append(i)
            break
    # Reverse
    for i in range(m)[::-1]:
        if lista[i].count(-1) == n:
            linesToRemove.append(i)
            break

    # Eliminate unusufuls columns
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

