A positive integer is considered uniform if all of its digits are equal. For example, 222222 is uniform, while 223223 is not.
Given two positive integers AA and BB, determine the number of uniform integers between AA and BB, inclusive.
Please take care to write a solution which runs within the time limit.
Constraints
1 \le A \le B \le 10^{12}1≤A≤B≤10 
12
 
Sample test case #1
A = 75
B = 300
Expected Return Value = 5
Sample test case #2
A = 1
B = 9
Expected Return Value = 9
Sample test case #3
A = 999999999999
B = 999999999999
Expected Return Value = 1
Sample Explanation
In the first case, the uniform integers between 7575 and 300300 are 7777, 8888, 9999, 111111, and 222222.
In the second case, all 99 single-digit integers between 11 and 99 (inclusive) are uniform.
In the third case, the single integer under consideration (999{,}999{,}999{,}999999,999,999,999) is uniform.





# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
    min_s, max_s = len(str(A)), len(str(B))

    min_val = int('1' * min_s)
    max_val = int('1' * max_s)
    if min_val == max_val:
        return B // max_val - (A - 1) // min_val
    return (max_s - min_s - 1) * 9 + 9 - ((A - 1) // min_val) + B // max_val

