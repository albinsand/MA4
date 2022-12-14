# Del 1 av MA4

from cmath import pi
import random
import matplotlib.pyplot as plt

# 1.1 - Approximation av pi med hjälp av Monte Carlo metoder

 

def MC_pi():
    n = [1000,10000,100000]

    pi_aprox_all = []

    n_cx_all = []
    n_cy_all = []

    n_sx_all = []
    n_sy_all = []

    for i in n:

        n_c_x = []
        n_c_y = []

        n_s_x = []
        n_s_y = []


        for x in range(1,i):
            n_cx = random.uniform(-1,1)
            n_cy = random.uniform(-1,1)   
            dist = (n_cx*n_cx)+(n_cy*n_cy)
            if dist <= 1:
                n_c_x.append(n_cx)
                n_c_y.append(n_cy)             
            else:
                n_s_x.append(n_cx)
                n_s_y.append(n_cy)

        pi_aprox = 4 * (len(n_c_x)/i)
        pi_aprox_all.append(pi_aprox)
    
        n_cx_all.append(n_c_x)
        n_cy_all.append(n_c_y)
        n_sx_all.append(n_s_x)
        n_sy_all.append(n_s_y)

    #print(pi_aprox_all)

    for i in range(0,3):
        plt.plot(n_cx_all[i],n_cy_all[i],'ro',n_sx_all[i],n_sy_all[i],'bo')
        plt.axis([-1, 1, -1, 1])
        plt.title(f'n = {n[i]} and \u03C0 \u2245 {pi_aprox_all[i]}')
        plt.savefig(f'piaprox-{n[i]}.png')
        
   
#print(MC_pi())

# 1.2 Approximera volymen av en d-dimensionell hypersfär

import math

def sfar_multidim(n = 10000000,d = 11):

    cr = [list(map(lambda x : random.uniform(-1,1)**2,range(0,d))) for i in range(0,n)] 
    summa = list(map(sum,cr))
    n_sphere = list(filter(lambda z: z <= 1, summa)) 

    return (2 ** d) * len(n_sphere)/n 
                                           
                                        
def V_d(d):
    return math.pi**(d/2)/math.gamma((d/2)+1) 

#print('Uppgift 1.2')
#print(f'Apprximation for n = 1000000 och d = 2: {sfar_multidim(n = 100000,d = 2)} ,Enligt definition: {V_d(2)}') 
#print(f'Apprximation for n = 1000000 och d = 11: {sfar_multidim(n = 100000,d = 11)} ,Enligt definition: {V_d(11)}') 
'''
Uppgift 1.2

Apprximation for n = 1000000 och d = 2: 3.14208 ,Enligt definition: 3.141592653589793

Apprximation for n = 1000000 och d = 11: 2.00704 ,Enligt definition: 1.8841038793898994

'''

# 1.3 Parallel programmering

from time import perf_counter as pc
import concurrent.futures as future

def parall_sfar_multidim(n = 1000000,d = 11,pros = 10):

    var1 = [n // pros for _ in range(pros)]
    var2 = [d for _ in range(pros)] 

    with future.ProcessPoolExecutor() as ex:

        res = ex.map(sfar_multidim, var1,var2) 

    return sum(res)/pros

'''
Uppgift 1.3:

Kod fran 1.2, sfar_multidim(10000000, 11):

Tid for berakning:  168.41 sek
Approximerad volym: 1.885184
Verklig volym:      1.8841038793898994

Parallel prog, parall_sfar_multidim(10000000, 11, 10):

Tid for berakning : 6.29 sek
Approximerad volym: 1.9394559999999998 
Verklig volym:      1.8841038793898994

'''


if __name__ == '__main__':
  
# notera läggre n här, inte de värdena på n som ska testas i 1.3

    start = pc()
    sfar_multidim(100000, 11)
    end = pc()

    print('Uppgift 1.3:')

    print('Kod fran 1.2, sfar_multidim(10000000, 11):')
    print(f'Approximerad volym:{sfar_multidim(100000, 11)}, Verklig volym:{V_d(11)}')
    print(f"Tid for berakning: {round(end - start, 2)} sek")

    start = pc()
    parall_sfar_multidim(10000, 11, 10)
    end = pc()

    print('Parallel prog, parall_sfar_multidim(1000000, 11, 10):')
    print(f'Approximerad volym:{parall_sfar_multidim(10000, 11,10)}, Verklig volym:{V_d(11)}')
    print(f"Tid for berakning : {round(end - start, 2)} sek")
    
