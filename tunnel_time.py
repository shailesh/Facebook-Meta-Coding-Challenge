There’s a circular train track with a circumference of CC metres. Positions along the track are measured in metres, clockwise from its topmost point. For example, the topmost point is position 00, 11 metre clockwise along the track is position 11, and 11 metre counterclockwise along the track is position C-1C−1.
A train with negligible length runs clockwise along this track at a speed of 11 metre per second, starting from position 00. After CC seconds go by, the train will have driven around the entire track and returned to position 00, at which point it will continue going around again, with this process repeated indefinitely.
There are NN tunnels covering sections of the track, the iith of which begins at position A_iA 
i
​
  and ends at position B_iB 
i
​
  (and therefore has a length of B_i - A_iB 
i
​
 −A 
i
​
  metres). No tunnel covers or touches position 00 (including at its endpoints), and no two tunnels intersect or touch one another (including at their endpoints). For example, if there's a tunnel spanning the interval of positions [1, 4][1,4], there cannot be another tunnel spanning intervals [2, 3][2,3] nor [4, 5][4,5].
The train’s tunnel time is the total number of seconds it has spent going through tunnels so far. Determine the total number of seconds which will go by before the train’s tunnel time becomes KK.
Constraints
3 \le C \le 10^{12}3≤C≤10 
12
 
1 \le N \le 500{,}0001≤N≤500,000
1 \le A_i \lt B_i \le C-11≤A 
i
​
 <B 
i
​
 ≤C−1
1 \le K \le 10^{12}1≤K≤10 
12
 
Each test case's parameters will be formulated such that the correct answer for that case is at most 10^{15}10 
15
 .
Sample test case #1
C = 10
N = 2
A = [1, 6]
B = [3, 7]
K = 7
Expected Return Value = 22
Sample test case #2
C = 50
N = 3
A = [39, 19, 28]
B = [49, 27, 35]
K = 15
Expected Return Value = 35
Sample Explanation
In the first case, the train track (depicted below) has points 0...90...9, with one tunnel spanning the interval of positions [1, 3][1,3] and another spanning [6, 7][6,7]. In order to reach a tunnel time of 77, the train will need to go around the complete track twice and then stop at position 22. The total time taken in doing so is 10 + 10 + 2 = 2210+10+2=22 seconds.

In the second case, the train's tunnel time will reach 1515 seconds after 3535 seconds have passed, right as the train exits tunnel 33 (having previously gone through tunnel 22).




from typing import List
# Write any import statements here

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  # Write your code here
    # First handle full loops
    loop_ttime = sum(b-a for a,b in zip(A,B))
    res = C * (K // loop_ttime)
    K %= loop_ttime

    # If we finish right after the last tunnel
    if K == 0:
        return res - C + max(B)

    #print(f'{loop_ttime=}, {res=}, {K=}')
    # Then handle remainding
    for a, b in sorted(zip(A, B)):
        if b-a < K:
            K -= b-a
        else:
            end = a + K
            break
    res += end
    return res
