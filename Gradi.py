import numpy as np
from numpy import linalg as LA

Max=0 #si se va a maximizar entonces se define max=1 si se va a minimizar entonces se define max=0

f=lambda x1,x2: x1**2 + 2*x2**2 + 4*x1 - 4*x2  #Función
gx = lambda x1,x2 : 2*x1+4      #Gradiente
gy = lambda x1,x2 : 4*x2-4      #de la función

x=[1,2]  #punto inicial
Tol=2e-2  #tolerancia del algoritmo                       
MaxIter=100   #Maximo de iteraciones                     
bk=5 #límite superior para la búsqueda unidimensional

grad=[gx(x[0],x[1]) , gy(x[0],x[1])] #se evalua el gradiente en el punto inicial

Fgrad = np.array(grad)
x0=np.array(x)

if Max==1:
    Fgrad = Fgrad   # si se maximiza entonces se escoje el gradiente
else:
    Fgrad = -Fgrad # si se minimiza entonces se escoje el menos gradiente 

iter=0 # se inician las iteraciones

def AureaDer(f,x0,Fgrad,bk,Max) :  #Metodo aurea para hayar h
    ak=-5   
    tol=0.02
    alpha=0.618

    lamdak=alpha*ak+(1-alpha)*bk
    miuk=(1-alpha)*ak+alpha*bk 

    fl=f(x0[0]+lamdak*Fgrad[0],x0[1]+lamdak*Fgrad[1])
    fm=f(x0[0]+miuk*Fgrad[0],x0[1]+miuk*Fgrad[1])
    it=0
    while np.abs(bk-ak)>=tol:
        it+=1
        if Max==0:
            if fl>fm:
                ak=lamdak
                lamdak=miuk
                fl=fm
                miuk=(1-alpha)*ak+alpha*bk
                fm=f(x0[0]+miuk*Fgrad[0] , x0[1]+miuk*Fgrad[1])
            elif fl<fm:
                bk=miuk
                miuk=lamdak
                fm=fl
                lamdak=alpha*ak+(1-alpha)*bk
                fl=f(x0[0]+lamdak*Fgrad[0] , x0[1]+lamdak*Fgrad[1])
        if Max==1:
            if fl>fm:
                bk=miuk
                miuk=lamdak
                fm=fl
                lamdak=alpha*ak+(1-alpha)*bk
                fl=f(x0[0]+lamdak*Fgrad[0] , x0[1]+lamdak*Fgrad[1])                
            elif fl<fm:
                ak=lamdak
                lamdak=miuk
                fl=fm
                miuk=(1-alpha)*ak+alpha*bk
                fm=f(x0[0]+miuk*Fgrad[0] , x0[1]+miuk*Fgrad[1])

    h=(lamdak+miuk)/2
    return h

while LA.norm(Fgrad)>=Tol and iter<=MaxIter: #Inicio iteraciones del metodo del gradiente
    h=AureaDer(f,x0,Fgrad,bk,Max) #llamada al método unidimensional
    x0=x0+h*Fgrad; #se calcula el nuevo punto

    grad=[gx(x0[0],x0[1]) , gy(x0[0],x0[1])] # se evalua el gradiente en el punto  
    Fgrad = np.array(grad)

    if Max==1:
        Fgrad = Fgrad   # si se maximiza entonces se escoje el gradiente
    else:
        Fgrad = -Fgrad  # si se minimiza entonces se escoje el menos gradiente 

    iter+=1
    print("iter: ",iter,x0,Fgrad,h)