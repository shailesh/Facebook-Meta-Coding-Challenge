You are the manager of a mail room which is frequently subject to theft. A period of NN days is about to occur, such that on the iith day, the following sequence of events will occur in order:
A package with a value of V_iV 
i
​
  dollars will get delivered to the mail room (unless V_i = 0V 
i
​
 =0, in which case no package will get delivered).
You can choose to pay CC dollars to enter the mail room and collect all of the packages there (removing them from the room), and then leave the room
With probability SS, all packages currently in the mail room will get stolen (and therefore removed from the room).
Note that you're aware of the delivery schedule V_{1..N}V 
1..N
​
 , but can only observe the state of the mail room when you choose to enter it, meaning that you won't immediately be aware of whether or not packages were stolen at the end of any given day.
Your profit after the NNth day will be equal to the total value of all packages which you collected up to that point, minus the total amount of money you spent on entering the mail room.
Please determine the maximum expected profit you can achieve (in dollars).
Note: Your return value must have an absolute or relative error of at most 10^{-6}10 
−6
  to be considered correct.
Constraints
1 \le N \le 4{,}0001≤N≤4,000
0 \le V_i \le 1{,}0000≤V 
i
​
 ≤1,000
1\le C \le 1{,}0001≤C≤1,000
0.0 \le S \le 1.00.0≤S≤1.0
Sample test case #1
N = 5
V = [10, 2, 8, 6, 4]
C = 5
S = 0.0
Expected Return Value = 25.00000000
Sample test case #2
N = 5
V = [10, 2, 8, 6, 4]
C = 5
S = 1.0
Expected Return Value = 9.00000000
Sample test case #3
N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.5
Expected Return Value = 17.00000000
Sample test case #4
N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.15
Expected Return Value = 20.10825000
Sample Explanation
In the first case, packages will never be stolen. You should therefore enter the mail room just once, on the final day, at which point there are sure to be 55 packages there with a total value of 10 + 2 + 8 + 6 + 4 = 3010+2+8+6+4=30 dollars. Subtracting the 55-dollar fee for entering the mail room, your profit is guaranteed to be 30 - 5 = 2530−5=25 dollars.
In the second case, each package is sure to be stolen at the end of the day on which its delivered. You should enter the mail room on days 11, 33, and 44, each time collecting just the package delivered on that day. This yields a guaranteed profit of 10 + 8 + 6 - (3 * 5) = 910+8+6−(3∗5)=9 dollars.
In the third case, on each day, there's a 5050% chance that all packages in the mail room will be stolen. You should enter the mail room on days 11, 33, 44, and 55. Note that, when you enter on day 33, there will be a 5050% chance of the room having 22 packages (with values of 22 and 88 dollars), and a 5050% chance of the room having just 11 package (worth 88 dollars).
In the fourth case, you should only enter the mail room on days 11 and 55.



from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  # Write your code here
    evs = [0] # evs[i] = sum_{0 <= j < i} v[j]*(1-S)^{i-j-1}
    for v in V:
        evs.append(evs[-1]*(1-S) + v)
    dp = [0]*(N+1)
    for i in range(N-1, -1, -1):
        new = [0]*(N+1)
        for last_clear in range(i+1):
            ex_val = evs[i+1] - evs[last_clear]*(1-S)**(i-last_clear+1)
            new[last_clear] = max(ex_val - C + dp[i+1], dp[last_clear])
        dp = new
    return dp[0]


