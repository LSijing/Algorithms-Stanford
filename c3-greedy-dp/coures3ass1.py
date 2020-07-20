# -*- coding: utf-8 -*-

def weighted_complete_time(length, weight, ordering):
    t = 0
    weightedtime = 0
    for i in ordering:
        t += length[i]
        weightedtime += t * weight[i]
    return weightedtime

#num_file = '41_10000'
#f = open('stanford-algs-master/testCases/course3/assignment1SchedulingAndMST/questions1And2/input_random_'+num_file+'.txt')
#output = open('stanford-algs-master/testCases/course3/assignment1SchedulingAndMST/questions1And2/output_random_'+num_file+'.txt').readlines()
f = open('data/jobs.txt')


n = int(f.readline())
data = f.readlines()
weight = []
length = []
for s in data:
    idx = s.find(' ')
    weight.append(int(s[0:idx]))
    length.append(int(s[idx+1:]))
    
score = []
for x,y in zip(weight,length):
    score.append(x-y)
sortedindex = sorted( range(len(score)), key= lambda i: (score[i],weight[i]), reverse=True)

t1 = weighted_complete_time(length, weight, sortedindex)


score = []
for x,y in zip(weight,length):
    score.append(x/y)
ordering = sorted( range(len(score)), key=lambda i: score[i], reverse=True)
t2 = weighted_complete_time(length, weight, ordering)

#print(t1,t2,'\n',output)
print(t1,t2)
