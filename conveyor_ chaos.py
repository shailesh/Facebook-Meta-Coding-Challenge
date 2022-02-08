A distribution center moves packages around using a system of conveyor belts, which can be represented as line segments on the 2D Cartesian plane. The iith conveyor belt runs from coordinates (A_i, H_i)(A 
i
​
 ,H 
i
​
 ) to (B_i, H_i)(B 
i
​
 ,H 
i
​
 ). No two conveyor belts share any points in common, including endpoints or interior points. Gravity points in the direction of the negative y-axis, meaning that objects normally fall vertically downwards, with their y-coordinate decreasing over time.
Each conveyor belt runs to either the left or the right. A package can be considered to occupy a single point on the plane. If a package lands strictly within conveyor belt ii (excluding its endpoints), then it will be transported to its left or right end (either (A_i, H_i)(A 
i
​
 ,H 
i
​
 ) or (B_i, H_i)(B 
i
​
 ,H 
i
​
 )), depending on the conveyor belt's direction, before continuing to fall vertically downwards.
You'll start by selecting a single conveyor belt and choosing a fixed direction (either left or right) for it to run in. Then, random directions will be independently chosen for each of the remaining N - 1N−1 conveyor belts (each being either left or right with equal probability). Finally, a single package will be dropped into the system from high above, at coordinates (x, 1{,}000{,}000)(x,1,000,000), where xx is a real value drawn uniform randomly from the inclusive interval [0, 1{,}000{,}000][0,1,000,000]. Your objective is to minimize the expected horizontal distance which this package will travel along conveyor belts before hitting the ground (any point with y-coordinate 00).
For example, consider the following system of conveyor belts (as are present in the second sample case):

Consider picking the conveyor belt at y-coordinate 55 and causing it to run to the left. If it then so happens that the bottommost conveyor belt also runs to the left while the other three run to the right and the package falls at x-coordinate 3{,}0003,000, then the package will travel a total of 6{,}0006,000 units horizontally across conveyor belts, as illustrated below:

Determine the minimum achievable expected horizontal distance traveled by the package assuming an ideal initial choice of conveyor belt and direction.
Note: Your return value must have an absolute or relative error of at most 10^{-6}10 
−6
  to be considered correct.
Constraints
1 \le N \le 500{,}0001≤N≤500,000
1 \le H_i \le 999{,}9991≤H 
i
​
 ≤999,999
0 \le A_i \lt B_i \le 1{,}000{,}0000≤A 
i
​
 <B 
i
​
 ≤1,000,000
Sample test case #1
N = 2
H = [10, 20]
A = [100000, 400000]
B = [600000, 800000]
Expected Return Value = 155000.00000000
Sample test case #2
N = 5
H = [2, 8, 5, 9, 4]
A = [5000, 2000, 7000, 9000, 0]
B = [7000, 8000, 11000, 11000, 4000]
Expected Return Value = 36.50000000
Sample Explanation
In the first case, there are two conveyor belts, as depicted below:

You should pick the second conveyor belt and cause it to run to the right. Packages falling at x-coordinates in the intervals [0, 100{,}000][0,100,000] and [800{,}000, 1{,}000{,}000][800,000,1,000,000] will fall directly to the ground (with 0 horizontal travel distance), while packages falling at x-coordinates in the interval (400{,}000, 800{,}000)(400,000,800,000) will have an average horizontal travel distance of 200{,}000200,000 units. This leaves packages falling at x-coordinates in the interval (100{,}000, 400{,}000](100,000,400,000], which will have an average horizontal travel distance of either 150{,}000150,000 units (if the first conveyor belt runs to the left) or 350{,}000350,000 units (if it runs to the right). This yields an overall expected horizontal travel distance of 0 * 0.2 + 200{,}000 * 0.4 + ((150{,}000 + 350{,}000) / 2) * 0.3 = 155{,}0000∗0.2+200,000∗0.4+((150,000+350,000)/2)∗0.3=155,000, which is the minimum achievable expected horizontal travel distance.
The second case is depicted above. In it, you should pick the third conveyor belt and cause it to run to the left.








from typing import List
# Write any import statements here

def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:
  # Write your code here
    W = 1_000_000 # Width of space
    roots, G = make_graph(W, H, A, B)
    pss, prices = push_down(G, roots, A, B)

    expectation = 0
    for i, ps in enumerate(pss[:-1]):
        expectation += (B[i]-A[i])/2 * sum(w for _, w in ps)

    # We can always do at least as well as random (MOCP)
    best = expectation
    for i, ps in enumerate(pss[:-1]):
        # Now what happens if we force this belt left or right?
        # It means something to the time on the belt itself,
        # but we also need to know the expected time the package
        # travels after falling off the left and right side
        # respectively.
        a, b = A[i], B[i]
        left = sum((p-a)*w for p, w in ps)
        right = sum((b-p)*w for p, w in ps)

        totw = sum(w for _, w in ps)
        (i1, _), (i2, _) = G[i]
        price_left, price_right = prices[i1], prices[i2]

        val = expectation \
                - (B[i]-A[i] + price_left + price_right)/2 * totw \
                + min(left+price_left*totw, right+price_right*totw)
        best = min(best, val)

    return best/W

  
def make_graph(W, H, A, B):
  # We can make a list of up to N top-nodes, which represent where packages
  # can land, including weight.

  # We handle END before START to avoid end-point captures
  # If a package lands _strictly_ within conveyor belt i
  # (excluding its endpoints), then it will be transported
  # to its left or right end
  START, END = 1, 0
  events = [(a, START, -H[i], i) for i, a in enumerate(A)]
  events += [(b, END, H[i], i) for i, b in enumerate(B)]
  events.sort()

  fw = KeyedSegmentTree(2**20) # NOTE: must be larger than the max height
  MH = 10**6 # Add this value to all height to make them positive before putting in tree
  #fw = SegmentTreeBrute()
  G = [[(None, 0), (None, 0)] for _ in range(len(H)+1)]
  roots = []
  top_envelope_start = 0
  top_envelope_i = len(H)
  fw.add(len(H), MH+0) # Add the bottom
  #to_add = [] # Starts we haven't added yet to prevent accidential catching
  for p, typ, _, i in events:
      if typ == START:
          G[i][0] = (fw.next(MH-H[i]), p)
          fw.add(i, MH-H[i])
          # if i is the top it covers something else and starts a new root
          if fw.top() == i:
              roots.append((top_envelope_i, (top_envelope_start+p)/2, p-top_envelope_start))
              top_envelope_i = i
              top_envelope_start = p
      if typ == END:
          G[i][1] = (fw.next(MH-H[i]), p)
          fw.remove(i)
          if top_envelope_i == i:
              roots.append((i, (top_envelope_start+p)/2, p-top_envelope_start))
              top_envelope_i = fw.top()
              top_envelope_start = p
  assert top_envelope_i == len(H)
  roots.append((len(H), (top_envelope_start+W)/2, W-top_envelope_start))
  return roots, G
  
def push_down(G, roots, A, B):
    order = topsort(G)

    # All incoming positions and their probabilities when
    # conveyer belts are chosen at random.
    pss = [[] for _ in G]
    # Start by adding roots
    for (i, p, w) in roots:
        pss[i].append((p, w))
    # Go through graph in topological order,
    # ignore the bottom.
    for i in order[:0:-1]:
        W = sum(w for _, w in pss[i])
        (i1, p1), (i2, p2) = G[i]
        pss[i1].append((p1, W/2))
        pss[i2].append((p2, W/2))

    # Also compute prices, going the other way through the order
    # This is the expected price a package will pay when landing
    # (anywhere) on the conveyer belt
    prices = [0]*len(G)
    # Again, skip the bottom. The bottom is free.
    for i in order[1:]:
        (i1, _), (i2, _) = G[i]
        prices[i] = (B[i]-A[i])/2 + (prices[i1] + prices[i2])/2

    return pss, prices

def topsort(G):
    in_graph = [[] for _ in G]
    for i, ((i1, _), (i2, p)) in enumerate(G[:-1]):
        in_graph[i1].append(i)
        in_graph[i2].append(i)

    outs = [2] * (len(G)-1) + [0]
    ready = [len(G)-1]
    res = []
    while ready:
        i = ready.pop()
        res.append(i)
        for i1 in in_graph[i]:
            outs[i1] -= 1
            if outs[i1] == 0:
                ready.append(i1)
    return res
  
class KeyedSegmentTree:
  def __init__(self, size):
      self.t = SegmentTree(size)
      self.v2k = {}
      self.k2v = {}
  def add(self, k, v):
      self.t.set(v, 1)
      self.v2k[v] = k
      self.k2v[k] = v
  def remove(self, k):
      v = self.k2v.pop(k)
      del self.v2k[v]
      self.t.set(v, 0)
  def next(self, v):
      v1 = self.t.succ(v)
      return self.v2k[v1]
  def top(self):
      return self.next(-1)
    

class SegmentTree:
  def __init__(self, size):
    h = size.bit_length()
    assert size == 1 << h-1, 'Size must be power of 2'
    self.h = h
    self.last = [-1] * (1 << h)
    # Recall, children of i are 2i+1 and 2i+2
    # The parent of i is (i-1) >> 1
    # That makes the parent of 0 = (-1)>>1 = -1
    # Three tree at i has size 2**(h - (i+1).bit_length())

  def set(self, i, v):
    p = (1 << self.h-1) - 1 + i
    self.last[p] = 0 if v != 0 else -1
    p = (p-1) >> 1
    while p != -1:
        l, r = self.last[2*p+1], self.last[2*p+2]
        if l == -1 and r == -1:
            self.last[p] = -1
        elif r != -1:
            left_size = 1 << (self.h - (2*p+2).bit_length())
            self.last[p] = r + left_size
        else:
            self.last[p] = l
        p = (p-1) >> 1

  def succ(self, i):
    p = 0
    res = 0
    for _ in range(self.h-1):
        l, r = self.last[2*p+1], self.last[2*p+2]
        if l != -1 and l > i:
            p = 2*p+1
        else:
            left_size = 1 << (self.h - (2*p+2).bit_length())
            i -= left_size
            res += left_size
            p = 2*p+2
    return res
