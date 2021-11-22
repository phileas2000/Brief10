import math


def lin_reg1(liste):
    poids=[2.1,1.2,0.3,1.3]
    biais=3
    for i in range(len(liste)):
        liste[i]=liste[i]*poids[i]
    return sum(liste) + biais

def lin_reg2(liste):
    poids=[0.1,1.2,4.9,3.1]
    biais=-5
    for i in range(len(liste)):
        liste[i]=liste[i]*poids[i]
    return sum(liste) + biais

def lin_reg3(liste):
    poids=[0.4,2.6,2.5,3.8]
    biais=-8
    for i in range(len(liste)):
        liste[i]=liste[i]*poids[i]
    return sum(liste) + biais



def activation(x):
    if x >= 0:
        return x
    else:
        return 0


def linreg_next_layer(liste):
    poids=[1.1,-4.1,0.7]
    biais=5.1
    for i in range(len(liste)):
        liste[i]=liste[i]*poids[i]
    return sum(liste) + biais

def activation_next_layer(x):
    return 1/(1+math.exp(-x))

base= [1,-3.1,-7.2,2.1]
x = lin_reg1(base)
x1 = activation(x)
print("lin_reg1: "+str(x1))

x = lin_reg2(base)
x2 = activation(x)
print("lin_reg2: "+str(x2))

x = lin_reg3(base)
x3 = activation(x)
print("lin_reg3: "+str(x3))

x = linreg_next_layer([x1,x2,x3])
xf = activation_next_layer(x)
print("lin_reg final: "+str(xf))