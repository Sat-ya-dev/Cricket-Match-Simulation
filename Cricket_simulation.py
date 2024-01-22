import numpy as np
import random
import pandas
import re

#(a)
def action(b,w,A,i): #b=balls left, w=wickets left,A=set of possible shots,i=index corresponding to a shot in A
    𝑝𝑂𝑢𝑡𝑀𝑖𝑛=[0.01,0.02,0.03,0.1,0.3] 
    𝑝𝑂𝑢𝑡𝑀𝑎𝑥=[0.1,0.2,0.3,0.5,0.7]
    pout = 𝑝𝑂𝑢𝑡𝑀𝑎𝑥[i]-((𝑝𝑂𝑢𝑡𝑀𝑎𝑥[i]-𝑝𝑂𝑢𝑡𝑀𝑖𝑛[i])*(𝑤-1)/9)
    out = random.choices([1,0],weights = (pout,1-pout),k=1)[0]  #random.choices gives a list of k(here k=1) elements.calling the first element
    prun = 0.5 +(0.3)*((w-1)/9)
    run = random.choices([A[i],0],weights = (prun,1-prun),k=1)[0]  #run = a[i] or 0 with the prob prun and 1-prun respectively
    if(out==1):
        w=w-1
        r=0
    else:
        r=run
    b=b-1
    return [r,b,w]  # run per ball, balls left, wickets left
w=10
b=300
runs=0
A=[1,2,3,4,6]
l=[]
while not w==0 and b>0: # stop when wickets left is zero or balls left is zero
    i = random.choice(range(0,5)) # randomly selecting a shot possibility from A
    l=action(b,w,A,i)
    b=l[1]
    w=l[2]
    run_per_ball=l[0]
    runs += l[0]
    print("player scored",run_per_ball,"on",(300-b),"the ball with",w,"wickets left. Total runs are",runs,"with",b,"balls left")

#(b)
def game_avg(W): # finding avg for player (11-W,12-W)
    w=W
    b=300
    runs=0
    balls=0
    avg=0
    bavg=0
    l=[]
    for i in range(1000): # taking average of runs and balls played in 1000 matches
        while not w==(W-1) and b>0:
            l=action(b,W,A,0)  # i=0 because only runs allowed are 0 or 1
            b=l[1]
            w=l[2]
            balls+=1
            runs += l[0]
        avg+=runs
        bavg+=balls
    avg/=1000
    bavg/=1000
    print("average runs scored by Player",(11-W,12-W)," = ",avg)
    print("average balls played = ",bavg)

game_avg(10) # Player (1, 2) 
game_avg(1)  # Player (10, 11)

# (c)
def game_avg(W):
    w=W
    b=300
    runs=0
    balls=0
    avg=0
    bavg=0
    for i in range(1000):
        while not w==(W-1) and b>0:
            l=action(b,W,A,4) # i=4 because only runs allowed are 6 or 0
            b=l[1]
            w=l[2]
            balls+=1
            runs += l[0]
        avg+=runs
        bavg+=balls
    avg/=1000
    bavg/=1000
    print("average runs scored by Player",(11-W,12-W)," = ",avg)
    print("average balls played = ",bavg)
game_avg(10)
game_avg(1)

#(d)
A=[1,2,3,4,6]
for i in range(5):
    Run=[]
    avg=0
    for j in range(10):
        w=10
        b=300
        runs=0
        l=[]
        while not w==0 and b>0:
            l=action(b,w,A,i)
            b=l[1]
            w=l[2]
            run_on_shot=l[0]
            runs += l[0]
        Run.append(runs)
        avg+=runs
        avg/=10
    print("for stratergy",A[i]," runs scored in ten matches are : ",Run)
    print("the average runs in 10 matches are : ",avg)

