You're trying to open a lock. The lock comes with a wheel which has the integers from 11 to NN arranged in a circle in order around it (with integers 11 and NN adjacent to one another). The wheel is initially pointing at 11.
For example, the following depicts the lock for N = 10N=10 (as is presented in the second sample case).

It takes 11 second to rotate the wheel by 11 unit to an adjacent integer in either direction, and it takes no time to select an integer once the wheel is pointing at it.
The lock will open if you enter a certain code. The code consists of a sequence of MM integers, the iith of which is C_iC 
i
​
 . Determine the minimum number of seconds required to select all MM of the code's integers in order.
Please take care to write a solution which runs within the time limit.
Constraints
3 \le N \le 50{,}000{,}0003≤N≤50,000,000
1 \le M \le 1{,}0001≤M≤1,000
1 \le C_i \le N1≤C 
i
​
 ≤N
Sample test case #1
N = 3
M = 3
C = [1, 2, 3]
Expected Return Value = 2
Sample test case #2
N = 10
M = 4
C = [9, 4, 4, 8]
Expected Return Value = 11
Sample Explanation
In the first case, there are 33 integers on the lock, and the sequence of integers to be selected is [1, 2, 3][1,2,3]. One optimal way to enter the code is: select 11 \rightarrow→ rotate to 22 (11 second) \rightarrow→ select 22 \rightarrow→ rotate to 33 (11 second) \rightarrow→ select 33. The total time taken is 1 + 1 = 21+1=2 seconds.
In the second case, the lock consists of the integers 11 through 1010, and the sequence to be selected is [9, 4, 4, 8][9,4,4,8]. One optimal way to enter the code is: rotate from 11 backwards to 99 (22 seconds) \rightarrow→ select 99 \rightarrow→ rotate forwards to 44 (55 seconds) \rightarrow→ select 44 twice \rightarrow→ rotate forwards to 88 (44 seconds) \rightarrow→ select 88. The total time taken is 2 + 5 + 4 = 112+5+4=11 seconds.


from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
    count = 0
    previous = 1
    for i in C:
        count += min((previous - i) % N, (i - previous) % N)
        previous = i
    return count
