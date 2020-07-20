# -*- coding: utf-8 -*-

def int_plus(x,y):
    n = max(len(x), len(y))
    s,t = x.zfill(n), y.zfill(n)
    ten = 0
    res = ''
    for i in range(n):
        tmp = str(int(s[-i-1]) + int(t[-i-1]) + ten).zfill(2)
        ten = int(tmp[0])
        res = tmp[-1] + res
    if ten == 1:
        res = '1' + res
    return res

def int_minus(x,y):
    n = max(len(x),len(y))
    if x.zfill(n)>= y.zfill(n):
        s,t = x.zfill(n), y.zfill(n)
        sign = '+'
    else:
        t,s = x.zfill(n), y.zfill(n)
        sign = '-'
    ten = 0
    res = ''
    for i in range(n):
        tmp = int(s[-i-1]) - int(t[-i-1]) - ten
        if tmp<0:
            ten = 1
            tmp += 10
        else:
            ten = 0
        res = str(tmp) + res
    while res.startswith('0') and len(res)>1:
        res = res[1:]
    if sign == '-':
        return sign+res
    else:
        return res

def int_mul(x,y):
#    while x.startswith('0') and len(x)>1:
#        x = x[1:]
#    while y.startswith('0') and len(y)>1:
#        y = y[1:]
    n1, n2 = len(x), len(y)
    if n1!=n2:
        print('length error')
        return
    if n1==1:
        return str(int(x) * int(y)).zfill(2)
    n = n1//2
    a,b = x[0:n], x[n:]
    c,d = y[0:n], y[n:]
    ac = int_mul(a,c)
    ac = ac.ljust(2*n+len(ac),'0').zfill(4*n)
    bd = int_mul(b,d).zfill(4*n)
    abcd = int_plus(int_mul(a,d),int_mul(b,c))
    abcd = abcd.ljust(n+len(abcd),'0').zfill(4*n)
    res = int_plus(int_plus(ac,abcd),bd)
    return(res)
    
    
if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
#    x,y = 3141592653589793, 2718281828459045
    k = int_mul(str(x),str(y))
    print(k)
    print(int(k)-x*y)