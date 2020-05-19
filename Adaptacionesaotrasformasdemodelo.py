import numpy as np

c=[70,80,85]
A_ub=[[1,4,8],[40,30,20],[3,2,4]]
b_ub=[4500,36000,2700]
A_eq=[[1,1,1]]
b_eq=[999]

for x in range(1, 3):
    for y in range(0, 3):    
         A_ub[x][y] = A_ub[x][y]*-1
print(A_ub)   

for x in range(1, 3):  
     b_ub[x] = b_ub[x]*-1
print(b_ub)   

newRow = [0,0,0]

for x in range(0, 3):
    for y in range(0, 3):    
          print(A_ub[x][y],x,y)
          newRow[x] = newRow[x] + A_ub[y][x]
print('new row: ',newRow) 

newRow.append(0)

for x in range(1, 3):  
     newRow[3] = newRow[3] + b_ub[x]
print(newRow)

A_ub.insert(0, newRow)
del A_ub[1]

for x in range(1, 3):  
     A_ub[x].append(b_ub[x])

""" Metodo simplex """        
matrix = np.array(A_ub)
filas=len(matrix) 
columnas=len(matrix[0]) 
cPivote = 0
fPivote = 0

ultColumna = columnas-1

sw = 1
nMenor=1
while sw == 1:
    mNegativo = 9999 
    print ("inicio")

    for c in range(0,columnas):
        if matrix[0,c] < mNegativo:
            mNegativo = matrix[0,c] 
            cPivote = c

    for f in range(1,filas):
        if matrix[f,ultColumna]/matrix[f,cPivote] < nMenor: 
            nMenor = matrix[f,ultColumna] / matrix[f,cPivote]

            fPivote = f
    nPivote = matrix[fPivote,cPivote] 
    
    for c in range(0,columnas):
        matrix[fPivote,c] = matrix[fPivote,c] / nPivote

    for f in range(0,filas):
        factor = matrix[f,cPivote] 
        if f != fPivote:
            for c in range(0,columnas):
                matrix[f,c] = matrix[f,c] - (matrix[fPivote,c] * factor)

    for f in range (0,filas):
        print (matrix[f,:])

    mNegativo = 0
    for c in range(0,columnas):
        valor = matrix[0,c]
        if valor < mNegativo:
            mNegativo = valor

    if mNegativo < 0:
        sw = 1 
    else:
        sw = 0 
print("Finalizado.")