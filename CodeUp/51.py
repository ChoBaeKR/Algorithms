# 병합 정렬
# dd
# def 병합정렬(입력리스트):
#     입력리스트길이 = len(입력리스트)
#     if 입력리스트길이 <= 1:
#         return 입력리스트
#     중간값 = 입력리스트길이 // 2
#     그룹_하나 = 병합정렬(입력리스트[:중간값])
#     그룹_둘 = 병합정렬(입력리스트[중간값:])
#     print(f'그룹하나:{그룹_하나}\n그룹둘:{그룹_둘}')
#     결과값 = []
#     print(f'what ?: {그룹_하나 and 그룹_둘}')
#     while 그룹_하나 and 그룹_둘:
#         if 그룹_하나[0] < 그룹_둘[0]:
#             결과값.append(그룹_하나.pop(0))
#             print(f'if 그룹하나<그룹둘:{결과값}')
#         else:
#             결과값.append(그룹_둘.pop(0))
#             print(f'if 그룹하나>그룹둘:{결과값}')

#     while 그룹_하나:
#         결과값.append(그룹_하나.pop(0))
#         print(f'while 그룹하나:{결과값}')
#     while 그룹_둘:
#         결과값.append(그룹_둘.pop(0))
#         print(f'while 그룹둘:{결과값}')
#     return 결과값

# 주어진리스트 = [180, 145, 165, 45, 170, 175, 173, 171]
# 주어진리스트 = [int(i) for i in 주어진리스트]

# print(병합정렬(주어진리스트))

a = [1, 2, 3, 4]
b = []
while a:
    b.append(a.pop())
    print(b)
