You've found yourself in a grid of cells with RR rows and CC columns. The cell in the iith row from the top and jjth column from the left contains one of the following (indicated by the character G_{i,j}G 
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
  = "S", the cell contains your starting position. There is exactly one such cell.
If G_{i,j}G 
i,j
​
  = "E", the cell contains an exit. There is at least one such cell.
If G_{i,j}G 
i,j
​
  = "#", the cell contains a wall.
Otherwise, if G_{i,j}G 
i,j
​
  is a lowercase letter (between "a" and "z", inclusive), the cell contains a portal marked with that letter.
Your objective is to reach any exit from your starting position as quickly as possible. Each second, you may take either of the following actions:
Walk to a cell adjacent to your current one (directly above, below, to the left, or to the right), as long as you remain within the grid and that cell does not contain a wall.
If your current cell contains a portal, teleport to any other cell in the grid containing a portal marked with the same letter as your current cell's portal.
Determine the minimum number of seconds required to reach any exit, if it's possible to do so at all. If it's not possible, return -1−1 instead.
Constraints
1 \le R, C \le 501≤R,C≤50
G_{i,j} \inG 
i,j
​
 ∈ {".", "S", "E", "#", "a"..."z"}
Sample test case #1
R = 3
C = 3
G = .E.
    .#E
    .S#
Expected Return Value = 4
Sample test case #2
R = 3
C = 4
G = a.Sa
    ####
    Eb.b
Expected Return Value = -1
Sample test case #3
R = 3
C = 4
G = aS.b
    ####
    Eb.a
Expected Return Value = 4
Sample test case #4
R = 1
C = 9
G = xS..x..Ex
Expected Return Value = 3
Sample Explanation
In the first case, you can reach an exit in 44 seconds by walking left once, then up twice, and then finally right once.
In the second case, you can never reach the exit.
In the third case, you should walk right twice, then teleport to the cell in the 3rd row and 2nd column, and finally walk left once.
In the fourth case, you should walk left once, teleport to the cell in the last column, and walk left once more.




from typing import List
# Write any import statements here

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  # Write your code here
   portals = {}
   start = []
   for r, row in enumerate(G):
      for c, cell in enumerate(row):
         if 'a' <= cell <= 'z':
            portals.setdefault(cell, []).append((r, c))
         elif cell == 'S':
            start = [(r, c)]
            seen = {(r, c)}
   if not start:
      return -1
   return traverse(G, portals, start, seen)

def traverse(maze, portals, ns, seen):
   nn = []
   path = 1
   while ns:
      r, c = ns.pop()
      cell = maze[r][c]
      neigh = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] + portals.get(cell, [])
      for n in neigh:
         r, c = n
         cell = maze[r][c] if 0 <= r < len(maze) and 0 <= c < len(maze[r]) else '#'
         if cell == '#' or n in seen:
            continue
         if cell == 'E':
            return path
         seen.add(n)
         nn.append(n)

      if not ns:
         path += 1
         ns = nn
         nn = []
   return -1

