import sympy as sp
import numpy as np

(x, y, t) = sp.symbols('x,y,t') # t is equal to lambda, which is Lagrange

function = x**2+x*y+y**2
restriction = (x**2+y**2-1)
restrictionlambda = t*restriction
print("F(x,y) =",function)
print("G(x,y) =",restriction)
Dx = function.diff(x)
Dy = function.diff(y)
DxWithLambda = Dx - restrictionlambda.diff(x)
DyWithLambda = Dy - restrictionlambda.diff(y)
points=[] 
print("")
print("Derivada con respecto a x:",Dx)
print("Derivada con respecto a y:",Dy)
SDx =sp.solve(Dx,y) #Clears the y
ry=Dy.replace(y,SDx[0])# Replance the y with the result of SDx

x1=sp.solve(ry)#point x1
rx=Dx.replace(x,x1[0]) #Now we replace the x with the result of the other equation
y1=sp.solve(rx)#point y1
q=[x1[0],y1[0]]
points.append(q)
px = sp.solve(DxWithLambda) #Clears the function variable
py = sp.solve(DyWithLambda)
print("")
print("Derivada con respecto a x con lambda:",DxWithLambda)
print("Derivada con respecto a y con lambda:",DyWithLambda)
print("")
a = -py[0][t]+px[0][t] #We equalize the Lambda(t)

s= restriction.replace(x,y)
sy= sp.solve(s)#Solution for y
sx = sp.solve(a.subs(x,sy[0]))#Solution for x

for i in sy:
    q=[]
    for j in sx:
        q=[i,j]
        points.append(q) 
print("Puntos soluciones")    
print(points)
c=0
PointsSolutions=[]
#Here we are finding the points with the function
for i in points:
   s = function.subs(x,i[0])
   s1= s.subs(y,i[1])
   PointsSolutions.append(s1)
print("Remplazo de puntos soluciones en la funcion")   
print(PointsSolutions)
PointsLambda=[]

d=px[0][t]#Finding the lambda points from each point    
for i in points:
    u = d.subs(x,i[0])
    u1= u.subs(y,i[1])
    PointsLambda.append(u1)
print("Lambda en cada uno de los puntos",PointsLambda)
print("")

 #Hessiano Orlado

H = np.zeros((3,3))
c = 0
mins = []
maxs = []
pointsMax = []
pointsMin = []
for i in points:
    H[0][0]=0
    H[0][1] = -restriction.diff(x).subs(x,i[0])
    H[0][2] = -restriction.diff(y).subs(y,i[1])
    H[1][0] = -restriction.diff(x).subs(x,i[0])
    H[1][1] = DxWithLambda.diff(x).subs(t,PointsLambda[c])
    H[1][2] = DxWithLambda.diff(y).subs(y,i[1])
    H[2][0] = -restriction.diff(y).subs(y,i[1])
    H[2][1] = DyWithLambda.diff(x).subs(x,i[0])
    H[2][2] = DyWithLambda.diff(y).subs(t,PointsLambda[c])
    #print(H)
    #print(np.linalg.det(H))
    #Si el determinante de H > 0 es Maximo,
    #Si H < 0 es Minimo
    #Si H = 0 no determina nada
    if(np.linalg.det(H)<0):
        mins.append(PointsLambda[c])
        pointsMin.append(i)
    elif (np.linalg.det(H)>0):
        maxs.append(PointsLambda[c])
        pointsMax.append(i)
    c=c+1
print("Punto(s) maximo(s) ",pointsMax)
print("Punto(s) maximo(s) con lambda igual a ",maxs)
print("")
print("Punto(s) minimo(s) ",pointsMin)
print("Punto(s) minimo(s) con lambda igual a  ",mins)