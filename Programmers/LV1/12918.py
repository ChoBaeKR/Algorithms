# 문자열 다루기 기본
def solution(s):
    answer = False
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        answer = True
    return answer