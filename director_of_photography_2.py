Note: Chapter 1 is an easier version of this puzzle. The only difference is a smaller constraint on NN.
A photography set consists of NN cells in a row, numbered from 11 to NN in order, and can be represented by a string CC of length NN. Each cell ii is one of the following types (indicated by C_iC 
i
​
 , the iith character of CC):
If C_iC 
i
​
  = “P”, it is allowed to contain a photographer
If C_iC 
i
​
  = “A”, it is allowed to contain an actor
If C_iC 
i
​
  = “B”, it is allowed to contain a backdrop
If C_iC 
i
​
  = “.”, it must be left empty
A photograph consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered artistic if the distance between the photographer and the actor is between XX and YY cells (inclusive), and the distance between the actor and the backdrop is also between XX and YY cells (inclusive). The distance between cells ii and jj is |i - j|∣i−j∣ (the absolute value of the difference between their indices).
Determine the number of different artistic photographs which could potentially be taken at the set. Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.
Constraints
1 \le N \le 300{,}0001≤N≤300,000
1 \le X \le Y \le N1≤X≤Y≤N
Sample test case #1
N = 5
C = APABA
X = 1
Y = 2
Expected Return Value = 1
Sample test case #2
N = 5
C = APABA
X = 2
Y = 3
Expected Return Value = 0
Sample test case #3
N = 8
C = .PBAAP.B
X = 1
Y = 3
Expected Return Value = 3
Sample Explanation
In the first case, the absolute distances between photographer/actor and actor/backdrop must be between 11 and 22. The only possible photograph that can be taken is with the 33 middle cells, and it happens to be artistic.
In the second case, the only possible photograph is again taken with the 33 middle cells. However, as the distance requirement is between 22 and 33, it is not possible to take an artistic photograph.
In the third case, there are 44 possible photographs, illustrated as follows:
.P.A...B
.P..A..B
..BA.P..
..B.AP..
All are artistic except the first, where the artist and backdrop exceed the maximum distance of 33.






# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here  
  return solveBAP(N, C, X, Y) + solveBAP(N, C[::-1], X, Y)

def solveBAP(N, C, X, Y):
    b = 0
    p = C[X-1:Y].count('P')
    res = 0
    for i, c in enumerate(C):
        if i-X >= 0 and C[i-X] == 'B': b += 1
        if i-Y-1 >= 0 and C[i-Y-1] == 'B': b -= 1
        if i+X-1 < N and C[i+X-1] == 'P': p -= 1
        if i+Y < N and C[i+Y] == 'P': p += 1
        #print(i, C[i], p, b)
        if c == 'A': res += b * p
    return res
    
