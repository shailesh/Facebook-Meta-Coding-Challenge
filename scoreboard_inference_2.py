Note: Chapter 1 is an easier version of this puzzle. The only difference is a smaller set of possible problem point values.
You are spectating a programming contest with NN competitors, each trying to independently solve the same set of programming problems. Each problem has a point value, which is either 1, 2, or 3.
On the scoreboard, you observe that the iith competitor has attained a score of S_iS 
i
​
 , which is a positive integer equal to the sum of the point values of all the problems they have solved.
The scoreboard does not display the number of problems in the contest, nor their point values. Using the information available, you would like to determine the minimum possible number of problems in the contest.
Constraints
1 \le N \le 500{,}0001≤N≤500,000
1 \le S_i \le 1{,}000{,}000{,}0001≤S 
i
​
 ≤1,000,000,000
Sample test case #1
N = 5
S = [1, 2, 3, 4, 5]
Expected Return Value = 3
Sample test case #2
N = 4
S = [4, 3, 3, 4]
Expected Return Value = 2
Sample test case #3
N = 4
S = [2, 4, 6, 8]
Expected Return Value = 4
Sample test case #4
N = 1
S = [8]
Expected Return Value = 3
Sample Explanation
In the first case, it's possible that there are as few as 33 problems in the contest, for example with point values [1, 1, 3][1,1,3]. The 55 competitors could have solved the following subsets of problems:
Problem 11 (11 point)
Problems 11 and 22 (1 + 1 = 21+1=2 points)
Problem 33 (33 points)
Problems 22 and 33 (1 + 3 = 41+3=4 points)
All 33 problems (1 + 1 + 3 = 51+1+3=5 points)
It is impossible for all 55 competitors to have achieved their scores if there are fewer than 33 problems.
In the second case, one optimal set of point values is [1, 3][1,3].
In the third case, one optimal set of point values is [2, 2, 2, 2][2,2,2,2].
In the fourth case, one optimal set of point values is [2, 3, 3][2,3,3].





from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
    res = max(S)
    for ones in [0,1]:
        for twos in [0,1,2]:
            m = max(S) // 3
            for threes in [m, m-1, m-2]:
                if threes >= 0:
                    if all(test(s, ones, twos, threes) for s in S):
                        res = min(res, ones+twos+threes)
    return res

def test(s, ones, twos, threes):
    for i in range(ones+1):
        for j in range(twos+1):
            sr = s - (i + 2*j)
            if sr >= 0 and sr % 3 == 0 and sr//3 <= threes:
                return True
    return False



