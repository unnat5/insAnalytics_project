
# coding: utf-8

# In[609]:


import numpy as np


# In[108]:


## Question 1
## Max Sum square
class Question1():
    def __init__(self,matrix):
        self.matrix = matrix
        self.row,_ = matrix.shape
        self.temp = 0
    def find_max_sum_matrix(self):
        row = self.row
        x = self.matrix
        temp = self.temp
        for i in range(2,row):
            steps = ((row-i)/1) + 1
            t = 0
            for k in range(int(steps)):
                u = 0
                if k != 0:
                    t+=1
                for j in range(int(steps)):
                    if j != 0:
                        u+= 1
                    matrix = x[t:t+i,u:u+i]
                    #print("-"*10)
                    if np.sum(matrix)>temp:
                        final_max = matrix
                        temp = np.sum(matrix)
                        
        return final_max,temp


# In[610]:


x = np.random.randint(-9,9,(8,8))
print(x)


# In[360]:



max_matrix=Question1(x)
matrix, sum_ = max_matrix.find_max_sum_matrix()
print(matrix)
print(sum_)


# In[361]:


x = [[2,-8,4,-6],
     [7,1,-5,3],
     [-9,7,6,5],
     [8,3,2,-4]]


# In[362]:


x = np.array(x)


# In[363]:


max_matrix=Question1(x)
matrix, sum_ = max_matrix.find_max_sum_matrix()
print(matrix)
print(sum_)


# In[488]:


# Question 2
## Build the subsequences
def string_combinations(str_):
    ls = []
    string = [i for i in str_]
    for i in range(len(string)):
        q = string[i]
        for j in range(len(string)):
            for k in range(len(string)):
                
                t = ''.join(string[j:k]+[q])
                if q and t not in ls :
                    test = string[j:k]+[q]
                    if len(set(test)) == len(test):
                        ls.append(t)
    return ls


# In[611]:


string = 'xyz'
outsub = string_combinations(string)
print(outsub)


# In[612]:


string = 'ab'
outsub2 = string_combinations(string)
print(outsub2)


# In[168]:


## Question 3
# Hungry Pizza Lover
n = 6
order_time = [4,6,7,8,1,3]
time_taken = [1,2,6,1,3,2]

ls = []
for i in range(n):
    ls.append([order_time[i]+time_taken[i],order_time[i],i+1])
    
ls = sorted(ls)
## if two orders take same time then which order was ordered first.
for k in range(n-1):
    if ls[k+1][0]==ls[k][0] and ls[k+1][1] < ls[k][1]:
        temp = ls[k]
        ls[k] = ls[k+1]
        ls[k+1] = temp
print('The required order sequence {}'.format(np.array(ls)[:,2]))


# In[303]:


## Question 4 
## Circular Substring Problem
import re
def find_substring(word,target):
    #generating regex expression
    ls = []
    all_lazy_match = '.*?'
    for i in target:
        ls.append('['+i+']')
        ls.append(all_lazy_match)
    expression = ''.join(ls[:-1])
    con_word = word*2 #concatenating the word with itself.
    f_word=re.findall(expression,con_word)
    lengths=[len(i) for i in f_word]
    if not lengths:
        return -1
    return min(lengths)


# In[613]:


outc = find_substring('hackerrank','krr')
print(outc)


# In[614]:


outc1 = find_substring('melody','ldym')
print(outc1)


# In[615]:


outc2 = find_substring('melody','insAnalytics')
print(outc2)


# In[352]:


# Question5
## Maximum tip calculator
def max_tip(a,b,x,y):
    """
    a: Possible tips for Ayush
    b: Possible tips for Ankit
    x: Number of customers Ayush can handle.
    y: Number of customers Ankit can handle.
    """
    zipped_list = list(zip(a,b))
    ls=sorted(zipped_list,reverse=True)

    ls_x = []
    ls_y = []
    for index,objects in enumerate(ls):
        ai,bi = objects
        if ai > bi and len(ls_x)<x:
            ls_x.append(ai)
            if len(ls_x)>x :
                del ls_x[ls_x.index(min(ls_x))]
        elif len(ls_y)< y:
            ls_y.append(bi)
            if len(ls_y)>y:
                del ls_y[ls_y.index(min(ls_y))]
        elif len(ls_x) < x and ai==bi:
            ls_x.append(ai)
    return sum(ls_x+ls_y)


# In[616]:


x=4;y=4
a = [1,4,3,2,7,5,9,6]
b = [1,2,3,6,5,4,9,8]

outmax = max_tip(a,b,x,y)
print(outmax)


# In[617]:


x=3;y=3
a = [1,2,3,4,5]
b = [5,4,3,2,1]

outmax1 = max_tip(a,b,x,y)
print(outmax1)


# In[606]:


# Questions 6 
## Job Sequence Problem
def job_sequence(job_list):
    dicts = {}
    lsd = []
    time = 1
    net_profit = 0
    counter = 0
    for i in range(0,len(job),3):
        id_,deadline,profit = job[i:i+3]
        lsd.append((profit,deadline,id_))
        if deadline in dicts.keys():
            dicts[deadline].append(profit)
        else:
            dicts[deadline] = [profit]
    ks = []

    sorted_key = sorted(set(lsd),reverse=True)
    for _,key,id_ in sorted_key:
        if key >=time and dicts[key] and id_ not in ks:
            dicts[key].sort()
            ks.append(id_)
            net_profit += dicts[key][-1]
            dicts[key].pop()
            time += 1
            counter += 1
    return counter,net_profit            


# In[618]:


job = [1,4,20,2,1,10,3,1,40,4,1,30]
out0 = job_sequence(job)
print(*out0)


# In[619]:


job = [1,2,100,2,1,19,3,2,27,4,1,25,5,1,15]
out = job_sequence(job)
print(*out)

