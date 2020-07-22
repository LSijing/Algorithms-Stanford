# -*- coding: utf-8 -*-

"""
divide-and-conquer integer multiplication, n*log(n) time.
"""


def int_plus(x,y):
    n = max(len(x), len(y))
    s,t = x.zfill(n), y.zfill(n)
    ten = 0
    sol = ''
    for i in range(n):
        tmp = str(int(s[-i-1]) + int(t[-i-1]) + ten).zfill(2)
        ten = int(tmp[0])
        sol = tmp[-1] + sol
    if ten == 1: sol = '1' + sol
    return sol

def int_minus(x,y):
    n = max(len(x),len(y))
    s,t = x.zfill(n), y.zfill(n)
    ten = 0
    sol = ''
    for i in range(n):
        tmp = int(s[-i-1]) - int(t[-i-1]) - ten
        if tmp < 0:
            ten = 1
            tmp += 10
        else:
            ten = 0
        sol = str(tmp) + sol
    while len(sol)>1 and sol.startswith('0'):
        sol = sol[1:]
    return sol

def int_mul(x,y):
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0: return '0'
    if n1 == 1 or n2 == 1: return str(int(x) * int(y) )
    
    n = max(n1,n2) // 2
    a,b = x[0:-n], x[-n:]
    c,d = y[0:-n], y[-n:]
    ac = int_mul(a,c)
    bd = int_mul(b,d)
    a_pls_b = int_plus(a,b) 
    c_pls_d = int_plus(c,d)
    ad_pls_bc = int_minus(int_minus(int_mul(a_pls_b,c_pls_d), ac), bd)
    sol = int_plus(ac + bd.zfill(2*n) , ad_pls_bc+''.join(['0' for i in range(n)]))
    return(sol)
    
    
if __name__ == '__main__':
    x = '314159265358979323374944592'
    y = '2718281828459045237486412516568814623153643891456536028747135266249775745645647093699959574966967627'
#    x,y = '3141592653589793', '27182818289045'
    k = int_mul(x,y)
    print(k)
    print(int(k)-int(x)*int(y))