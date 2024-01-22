# Cricket-Match-Simulation
Problem statement: Consider the following simplified variant of the first innings of a one-day cricket match. The innings consists of 300 balls and at any point of time, treat the pair of batsmen playing as a single player. That is, there are 10 players: (1, 2),(2, 3), . . . ,(10, 11) with exactly one of them batting. In each ball, there are 5 possible shots A = {1, 2, 3, 4, 6} and each of these shots is associated with a risk of the player getting out. This risk varies from player to player. The probabilities of getting out for Player (1, 2) is pOutM in = [0.01, 0.02, 0.03, 0.1, 0.3] and for Player (10, 11) is pOutM ax = [0.1, 0.2, 0.3, 0.5, 0.7], where the ith entry is for the ith action. If there are w wickets in hand, then use the formula pOut(a, w) = pOutM ax(a) − (pOutM ax(a) − pOutM in(a)) × (w − 1)/9) to calculate the probabilities of getting out for Player (11 − w, 11 − w + 1) where w ∈ [10]. Note that pOut(a, 1) = pOutM in(a) and pOut(a, 10) = pOutM ax(a). Taking pRunM in = 0.5, and pRunM ax = 0.8, when the player is not getting out, the probability of successfully obtaining the runs for that shot is given by pRun(w) = pRunM in + (pRunM ax − pRunM in) × ((w − 1)/9).

(a) Implement an environment that maintains the state st = (bt , wt) where bt is the balls left and wt is the wickets left at time t. Initialize the start state to s1 = (300, 10). Write a function that accepts input as at ∈ A and returns rt (the runs scored on that shot) and st , and also updates st+1.

(b) Play at = 1 for each t and find the average balls played and average runs scored by Player (1, 2) and Player (10, 11).

(c) Play at = 6 for each t and find the average balls played and average runs scored by Player (1, 2) and Player (10, 11).

(d) Simulate 10 matches, for different constant strategies like at = 1 for each t, at = 2 for each t, etc. and and find the average runs obtained in each of the strategies.
