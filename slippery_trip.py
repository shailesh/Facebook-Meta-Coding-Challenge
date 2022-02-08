There's a grid of cells with RR rows (numbered from 11 to RR from top to bottom) and CC columns (numbered from 11 to CC from left to right). The grid wraps around horizontally, meaning that column 11 is just to the right of column CC (and column CC is just to the left of column 11).
The cell in row ii and column jj initially contains one of the following (indicated by the character G_{i,j}G 
i,j
​
 ):
If G_{i,j}G 
i,j
​
  = ".", the cell is empty.
If G_{i,j}G 
i,j
​
  = "*", the cell contains a coin.
If G_{i,j}G 
i,j
​
  = ">", the cell contains an arrow pointing right.
If G_{i,j}G 
i,j
​
  = "v", the cell contains an arrow pointing down.
You may cyclically shift each row to the right as many times as you'd like (including not at all). Each such shift causes each of the row's cells to move 11 column to the right, with its rightmost cell (in column CC) wrapping around and moving to column 11.
After you've finished rotating the rows to your liking, you'll take a trip through the grid, starting by entering the cell at the top-left corner (in row 11 and column 11) downward from above the grid. Upon entering a cell, if it contains a coin that you haven't yet collected, you'll collect it. If it contains an arrow, your direction of travel will change to that of the arrow (either right or down). Either way, you'll then proceed to the next adjacent cell in your direction of travel. If you move rightward from column CC, you'll wrap around to column 11 in the same row, and if you move downward from row RR, you'll end your trip. Note that you may only collect each cell's coin at most once, that your trip might last forever, and that once you begin your trip you cannot shift the grid's rows further.
Determine the maximum number of coins you can collect on your trip.
Constraints:
2 \le R, C \le 400{,}0002≤R,C≤400,000
R*C \le 800{,}000R∗C≤800,000
G_{i,j} \inG 
i,j
​
 ∈ {".", "*", ">", "v"}
Sample test case #1
R = 3
C = 4
G = .***
    **v>
    .*..
Expected Return Value = 4
Sample test case #2
R = 3
C = 3
G = >**
    *>*
    **>
Expected Return Value = 4
Sample test case #3
R = 2
C = 2
G = >>
    **
Expected Return Value = 0
Sample test case #4
R = 4
C = 6
G = >*v*>*
    *v*v>*
    .*>..*
    .*..*v
Expected Return Value = 6
Sample Explanation
The first case is depicted below:

To collect the maximum number of coins, the grid can be rotated as follows, and traversed with the highlighted path (1, 1) \rightarrow (2, 1) \rightarrow (2, 2) \rightarrow (2, 3) \rightarrow (2, 4) \rightarrow (3, 4)(1,1)→(2,1)→(2,2)→(2,3)→(2,4)→(3,4), ultimately ending the trip:

The second case is depicted below:

To collect the maximum number of coins, the grid can be rotated as follows, and traversed with the highlighted path (1, 1) \rightarrow (2, 1) \rightarrow (3, 1) \rightarrow (3, 2) \rightarrow (3, 3) \rightarrow (3, 1) \rightarrow ...(1,1)→(2,1)→(3,1)→(3,2)→(3,3)→(3,1)→..., at which point you'll loop around row 33 indefinitely:

In the third case, you cannot collect any coins.
In the fourth case, you can collect at most 66 coins.





from typing import List
# Write any import statements here

def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
  # Write your code here
    down = 0 # Best coming down from last row
    for r in range(R-1, -1, -1):
        # First solve the case of coming from the left
        if 'v' not in G[r]:
            right = [G[r].count('*')]*C
        else:
            right = [0]*C
            i = G[r].index('v')
            for j in range(C):
                c = (i-j) % C
                g = G[r][c]
                if g == 'v':  right[c] = down
                if g in '>.': right[c] = right[(c+1)%C]
                if g == '*':  right[c] = 1 + right[(c+1)%C]
        # Then solve the case of coming from above
        new_down = 0
        for c, g in enumerate(G[r]):
            if g == '*':  new_down = max(new_down, 1 + down)
            if g in '.v': new_down = max(new_down, down)
            if g == '>':  new_down = max(new_down, right[c])
        down = new_down
    return down


