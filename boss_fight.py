There are NN warriors, the iith of which has a health of H_iH 
i
​
  units and can deal D_iD 
i
​
  units of damage per second. They are confronting a boss who has unlimited health and can deal BB units of damage per second. Both the warriors and the boss deal damage continuously -− for example, in half a second, the boss deals B/2B/2 units of damage.
The warriors feel it would be unfair for many of them to fight the boss at once, so they'll select just two representatives to go into battle. One warrior ii will be the front line, and a different warrior jj will back them up. During the battle, the boss will attack warrior ii until that warrior is defeated (that is, until the boss has dealt H_iH 
i
​
  units of damage to them), and will then attack warrior jj until that warrior is also defeated, at which point the battle will end. Along the way, each of the two warriors will do damage to the boss as long as they are undefeated.
Of course, the warriors will never prevail, but they'd like to determine the maximum amount of damage they could deal to the boss for any choice of warriors ii and jj before the battle ends.
Note: Your return value must have an absolute or relative error of at most 10^{-6}10 
−6
  to be considered correct.
Constraints
2 \le N \le 500{,}0002≤N≤500,000
1 \le H_i \le 1{,}000{,}000{,}0001≤H 
i
​
 ≤1,000,000,000
1 \le D_i \le 1{,}000{,}000{,}0001≤D 
i
​
 ≤1,000,000,000
1 \le B \le 1{,}000{,}000{,}0001≤B≤1,000,000,000
Sample test case #1
N = 3
H = [2, 1, 4]
D = [3, 1, 2]
B = 4
Expected Return Value = 6.500000
Sample test case #2
N = 4
H = [1, 1, 2, 100]
D = [1, 2, 1, 3]
B = 8
Expected Return Value = 62.750000
Sample test case #3
N = 4
H = [1, 1, 2, 3]
D = [1, 2, 1, 100]
B = 8
Expected Return Value = 62.750000
Sample Explanation
In the first case, there are 33 warriors with healths of [2, 1, 4][2,1,4] units, and the ability to deal [3, 1, 2][3,1,2] units of damage respectively. The boss does B = 4B=4 units of damage per second.
The optimal solution is to choose warrior 33 as the front line and warrior 11 as backup. Warrior 33 will be defeated after 11 second, dealing 22 units of damage during this time (meanwhile, warrior 11 will have dealt 33 units of damage). Warrior 11 will then step up and last for 0.50.5 seconds, while dealing another 1.51.5 units of damage along the way. The total damage dealt will then be 2 + 3 + 1.5 = 6.52+3+1.5=6.5 units.
In each of the second and third cases, it's possible for 62.7562.75 units of damage to be dealt to the boss, though with different configurations of warriors.






from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  # Write your code here
    # We ignore the issue of repeating the point as first.
    # Our new points are (H*D, D)
    # We sort by x/y, that is H.
    hds = sorted(zip(H, D))
    hdds = [(h*d,d) for h,d in hds]
    i1s = ghscan(hdds)
    p1s = [hdds[i] for i in i1s]
    # We make a second data structure for the next "layer" of points.
    s = set(i1s)
    inner = [i for i in range(N) if i not in s]
    if inner:
        i2s = ghscan([hdds[i] for i in inner])
        # Convert indices back to hdds space
        i2s = [inner[j] for j in i2s]
        p2s = [hdds[i] for i in i2s]
    else:
        i2s = None

    # Now use Graham scan to remove everything not on the hull...
    best = 0
    for i, (h1, d1) in enumerate(hds):
        #ideal0 = max(range(N), key=lambda k: ip((1,h1), hdds[k]))
        #ideal = max([k for k in range(N) if k != i],
                    #key=lambda k: ip((1,h1), hdds[k]))
        # find h2, d2 maximizing h2*d2 + h2*h1
        j1 = search(p1s, (1, h1))
        j = i1s[j1]
        #assert j == ideal0
        # If we get the same point back, we have to do some work
        # to find an alternative
        if i == j:
            #print(f'Need alternative {i=} {j=} {ideal0=} {ideal=}')
            candidates = []
            if j1-1 >= 0: candidates.append((i1s[j1-1], p1s[j1-1]))
            if j1+1 < len(i1s): candidates.append((i1s[j1+1], p1s[j1+1]))
            if i2s is not None:
                j = search(p2s, (1, h1))
                candidates.append((i2s[j], p2s[j]))
            j, _ = max(candidates, key=lambda i_p: ip((1,h1), i_p[1]))
        best = max(best, h1*d1 + h1*hdds[j][1] + hdds[j][0])

    return best/B

def ccw(o, p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    ox, oy = o
    return (p1x-ox)*(p2y-oy) - (p1y-oy)*(p2x-ox)

def ip(p1, p2):
    return p1[0]*p2[0] + p1[1]*p2[1]

def ghscan(ps):
    # Assumes this is sorted by y/x
    # ps.sort(key=lambda y/x)
    s = []
    for i, p in enumerate(ps):
        while len(s) > 1 and ccw(ps[s[-2]], ps[s[-1]], p) >= 0:
            s.pop()
        s.append(i)
    return s

def search(hull, x):
    l, r = 0, len(hull)-1
    while r - l > 2:
        m1 = (l+r)//2
        m2 = m1+1
        # assert l < m1 < m2 < r
        if ip(hull[m1], x) > ip(hull[m2], x):
            r = m2
        else: l = m1
    return max(range(l, r+1), key=lambda i: ip(hull[i], x))

