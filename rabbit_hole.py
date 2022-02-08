Note: Chapter 2 is a harder version of this puzzle.
You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia.
The encyclopedia consists of NN different web pages, numbered from 11 to NN. Each page ii contains nothing but a single link to a different page L_iL 
i
​
 .
A session spent on this website involves beginning on one of the NN pages, and then navigating around using the links until you decide to stop. That is, while on page ii, you may either move to page L_iL 
i
​
 , or stop your browsing session.
Assuming you can choose which page you begin the session on, what's the maximum number of different pages you can visit in a single session? Note that a page only counts once even if visited multiple times during the session.
Constraints
2 \le N \le 500{,}0002≤N≤500,000
1 \le L_i \le N1≤L 
i
​
 ≤N
L_i \ne iL 
i
​
 ≠i
Sample test case #1
N = 4
L = [4, 1, 2, 1]
Expected Return Value = 4
Sample test case #2
N = 5
L = [4, 3, 5, 1, 2]
Expected Return Value = 3
Sample test case #3
N = 5
L = [2, 4, 2, 2, 3]
Expected Return Value = 4
Sample Explanation
In the first case, you can visit all 44 pages in a single browsing session if you begin on page 33. For example, you can visit the sequence of pages 3 \rightarrow 2 \rightarrow 1 \rightarrow 43→2→1→4.
In the second case, you can only visit at most 33 different pages -− for example, the sequence of pages 3 \rightarrow 5 \rightarrow 23→5→2.
In the third case, you can only visit at most 44 different pages -− for example, the sequence of pages 5 \rightarrow 3 \rightarrow 2 \rightarrow 45→3→2→4.







from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
    L = [l-1 for l in L] # 0-index
    visited = [-1 for _ in range(N)]
    length = [0 for _ in range(N)]
    stack = []
    onstack = [False] * N
    def dfs(time, i):
        while not onstack[i] and not length[i]:
            stack.append(i)
            onstack[i] = True
            visited[i] = time
            time += 1
            i = L[i]

        # length[i] is only sat if this is a later dfs run and we are
        # discovering old information
        if not length[i]:
            # Everything in the loop gets the same 'length'
            i0 = i
            length[i0] = time-visited[i0]
            while onstack[i0]:
                length[i] = length[i0]
                i = stack.pop()
                onstack[i] = False

        # Everything else gets 'one more'
        while stack:
            i1 = stack.pop()
            length[i1] = length[i] + 1
            onstack[i1] = False
            i = i1

    for i in range(N):
        dfs(0, i)

    return max(length)
