def printTable(table):
    colwidth=len(table)*[0]
    for i in range(len(table)):
        for j in range(len(table[i])):
            k=len(table[i][j])
            if colwidth[i]<k:
                colwidth[i]=k
    print(colwidth)

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colwidth[j]),end=' ')
        print()
           
    
     
    
    

    
