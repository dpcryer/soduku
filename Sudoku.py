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

#
# See if there are sqaures where there is only one possible value. If so remove that value from other squares in the row, column, and block
#
def onlyonepossible():
    changed = False
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
                        if possibles[row][colblank][uniqueval]:
                            changed = True
                            possibles[row][colblank][uniqueval] = False
                for rowblank in range(9):     # remove value across the column
                    if rowblank <> row:
                        if possibles[rowblank][col][uniqueval]:
                            changed = True
                            possibles[rowblank][col][uniqueval] = False
                for rowsquare in range(3):    # remove value
                    for colsquare in range(3):
                        rowblank = 3*(row/3)+rowsquare
                        colblank = 3*(col/3)+colsquare
                        if rowblank <> row or colblank <> col:
                            if possibles[rowblank][colblank][uniqueval]:
                                changed = True
                                possibles[rowblank][colblank][uniqueval] = False
    return changed

#
# See if there rows/columns/blocks where a possible value only appears once. If so remove other possible values from that square
#
def onlyoneinrowcolblock():                    # Should run onlyonepossible() after this to tidy up the other possibles in the row/col/block
    changed = False
    for val in range(1,10):
        for position in range(9):

            rowcount =0                         # check for values being unique in the row
            colcount =0                         # check for values being unique in the column
            blockcount = 0                     # check for values being unique in the 3x3 block

            blockrow = position/3              # work out which 3x3 block we're working in
            blockcol = position-(3*blockrow)

            for count in range(9):
                if possibles[position][count][val]:
                    rowcount = rowcount+1
                    rowpos = count
                if possibles[count][position][val]:
                    colcount = colcount+1
                    colpos = count
                row = (3*blockrow)+count/3
                col = (3*blockcol)+count-3*(count/3)
                if possibles[row][col][val]:
                    blockcount = blockcount+1
                    rowblockpos = row
                    colblockpos = col

            for blankval in range(1,10):        # blank out the other possibles 
                if rowcount == 1 and blankval <> val:
                    if possibles[position][rowpos][blankval]:
                        changed = True
                        possibles[position][rowpos][blankval] = False
                if colcount == 1 and blankval <> val:
                    if possibles[colpos][position][blankval]:
                        changed = True
                        possibles[colpos][position][blankval] = False
                if blockcount == 1 and blankval <> val:
                    if possibles[rowblockpos][colblockpos][blankval]:
                        changed = True
                        possibles[rowblockpos][colblockpos][blankval] = False
                
    return changed


getstartpos()
resultstopossibles()

print
printresults()
print
printpossibles()
print

print "One in rowcolblock"
change = onlyoneinrowcolblock()
printpossibles()
print "Check for only instance in a row/col/block - changed: "+str(change)

change = True
while change:
    change = onlyonepossible()
    printpossibles()
    print "Check for only one possible in a square - changed: "+str(change)
