#dependencias 
import numpy as np
from f import f

def sol_rk4(vt,T0):
    
    #Declarando vetor de temperaturas
    T = np.array([T0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando T(i) pelo método de Euler modificado
    for t in vt:
        k1 = f(T[-1])
        k2 = f(T[-1]+(h/2)*k1)
        k3 = f(T[-1]+(h/2)*k2)
        k4 = f(T[-1]+h*k3)
        K = (1/6)*(k1+2*(k2+k3)+k4)
        Ti = T[-1]+h*K
        T = np.append(T,Ti)
        
    return T[0:T.shape[0]-1]
