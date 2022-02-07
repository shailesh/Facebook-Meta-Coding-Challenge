There's a multiple-choice test with NN questions, numbered from 11 to NN. Each question has 22 answer options, labelled A and B. You know that the correct answer for the iith question is the iith character in the string CC, which is either "A" or "B", but you want to get a score of 00 on this test by answering every question incorrectly.
Your task is to implement the function getWrongAnswers(N, C) which returns a string with NN characters, the iith of which is the answer you should give for question ii in order to get it wrong (either "A" or "B").
Constraints
1 \le N \le 1001≤N≤100
C_i \in \{``A", ``B"\}C 
i
​
 ∈{‘‘A",‘‘B"}
Sample test case #1
N = 3
C = ABA
Expected Return Value = BAB
Sample test case #2
N = 5
C = BBBBB
Expected Return Value = AAAAA
Sample Explanation
In the first case the correct answers to the 33 questions are A, B, and A, in that order. Therefore, in order to get them all wrong, the 33 answers you should give are B, A, and B, in that order.
In the second case the correct answers are all B, so you should answer each question with A.



# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
    out = [0]*N
    for i, element in enumerate(C):
        if element == 'A':
            temp = 'B'
        else:
            temp = 'A'
        out[i] = temp
    wrong_str = str(''.join(out))
    return(wrong_str)
