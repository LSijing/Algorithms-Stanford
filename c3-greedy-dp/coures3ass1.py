# -*- coding: utf-8 -*-

"""
compute weighted complete time using two orderings,
the 1st is difference: weight-length,
the 2nd is ratio: weight/length.
"""
def load_data(filename):
    f = open(filename)
    n = int(f.readline())
    data = f.readlines()
    f.close()
    weight = []
    length = []
    for line in data:
        s = line.split(' ')
        weight.append(int(s[0]))
        length.append(int(s[1]))
    return n,weight,length
    
def compute_weighted_complete_time(length, weight, ordering):
    t = 0
    weightedtime = 0
    for i in ordering:
        t += length[i]
        weightedtime += t * weight[i]
    return weightedtime

def scheduling(length, weight):
    score1 = []
    score2 = []
    for x,y in zip(weight, length):
        score1.append(x-y)
        score2.append(x/y)
    order1 = sorted(range(len(score1)), key= lambda i:(score1[i],weight[i]), reverse=True)
    order2 = sorted(range(len(score2)), key= lambda i:score2[i], reverse=True)
    t1 = compute_weighted_complete_time(length, weight, ordering=order1)
    t2 = compute_weighted_complete_time(length, weight, ordering=order2)
    return t1,t2

if __name__ == '__main__':
    f1 = 'jobs.txt'
    n,weight,length = load_data(f1)
    print(scheduling(length, weight))
    
