# -*- coding: utf-8 -*-


def mwis(weight):
    """
    maximum weighted independent sets
    """
    n = len(weight)
    d = [0]
    d.append(weight[0])
    for i in range(2,len(weight)+1):
        d.append( max(d[i-1], d[i-2]+weight[i-1]) )
    
    exist = ''
    i = n-1
    while i >=  0:
        if d[i+1] == d[i]:
            exist = '0' + exist
            i -= 1
        else:
            exist = '01' + exist
            i -= 2
    if i == -2:
        exist = exist[1:]
    return exist

if __name__ == '__main__':
    f = open('mwis.txt')
    n = int(f.readline())
    weight = []
    for i in range(n):
        data = f.readline()
        w = float(data)
        weight.append(float(w))
    f.close()
    sol = mwis(weight)
    pos = [1, 2, 3, 4, 17, 117, 517, 997]
    res = ''
    for i in pos:
        if i <= n:
            res = res + sol[i-1]
        else:
            res = res + '0'
            
    print(res)
