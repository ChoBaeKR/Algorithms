# 쉽게 푸는 문제
# 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

A, B = map(int, input().split())
solve = []
firstNum = 1
result = 0
while (len(solve) <= B):
    for i in range(firstNum):
        solve.append(firstNum)
    firstNum += 1


for i in range(A-1,B):
    print(solve[i])
    result += solve[i]
print(result)