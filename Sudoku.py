possibles = [[[True for x in range(10)] for y in range(9)] for z in range(9)]
results = [["-" for y in range(9)] for z in range(9)]


def printpossibles():
    print "+-------+-------+-------+-------+-------+-------+-------+-------+-------+"
    for row in range(9):
        for valrow in range(3):
            print "|",
            for col in range(9):
                for valcol in range(3):
                    val = 3*valrow+valcol+1
                    if possibles[row][col][val]:
                        print val,
                    else:
                         print "-",
                print "|",
            print
        print "+-------+-------+-------+-------+-------+-------+-------+-------+-------+"

def printresults():
    print "+===+===+===+===+===+===+===+===+===+"
    for row in range(9):
        print "|",
        for col in range(9):
            print results[row][col],
            if col%3 == 2:
                print "|",
            else:
                print ".",
        print
        if row%3 ==2:
            print "+===+===+===+===+===+===+===+===+===+"
        else:
            print "+---+---+---+---+---+---+---+---+---+"

def getstartpos():
    for row in range(9):
        promptline = "Row" + str(row) + ":"
        rowin = raw_input(promptline)
        for col in range(9):
            val = rowin[col:col+1]
            if val and val.isdigit():
                results[row][col] = int(val)

def resultstopossibles():
    for row in range(9):
        for col in range(9):
            if results[row][col] <> "-":
                for val in range(1,10):
                    if val <> int(results[row][col]):
                        possibles[row][col][val] = False

def onlyonepossible():
    for row in range(9):
        for col in range(9):
            numpossibles = 0
            for val in range(1,10):
                if possibles[row][col][val]:
                    numpossibles = numpossibles+1
                    uniqueval = val
            if numpossibles == 1:             # only one value possible
                for colblank in range(9):     # remove value across the row
                    if colblank <> col:
                        possibles[row][colblank][uniqueval] = False
                for rowblank in range(9):     # remove value across the column
                    if rowblank <> row:
                        possibles[rowblank][col][uniqueval] = False
                for rowsquare in range(3):    # remove value
                    for colsquare in range(3):
                        rowblank = 3*(row/3)+rowsquare
                        colblank = 3*(col/3)+colsquare
                        if rowblank <> row or colblank <> col:
                            possibles[rowblank][colblank][uniqueval] = False

getstartpos()
resultstopossibles()

print
printresults()
print
printpossibles()
print
onlyonepossible()
printpossibles()
print
for i in range(20):
    onlyonepossible()
printpossibles()
