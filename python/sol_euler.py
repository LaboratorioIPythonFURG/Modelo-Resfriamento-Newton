#dependências
import numpy as np
from f import f

def sol_euler(vt,T0):
    
    #Declarando vetor de temperaturas
    T = np.array([T0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando T(i) pelo método de Euler
    for t in vt:
        Ti = T[-1]+h*f(T[-1])
        T = np.append(T,Ti)
        
    return T[0:T.shape[0]-1]
