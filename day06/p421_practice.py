# 성적별로 조 편성하기 p421
# 학생 성적별로 정렬 후 가장 성적이 높은 학생과 가장 낮은 학생을 짝으로 조를 만들자. 전체 학생수는 짝수

## 클래스와 함수 선언 부분##
def scoreSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end,0,-1):
            if (ary[cur-1][1] > ary[cur][1]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary

## 전역 변수 선언 부분 ##
scoreAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

## 메인 코드 부분 ##
print(f'정렬 전 -> {scoreAry}')
scoreAry = scoreSort(scoreAry)
print(f'정렬 후 -> {scoreAry}')
print()

print('## 성적별 조 편성표 ##')
for i in range(len(scoreAry)//2):
    print(scoreAry[i][0], ':', scoreAry[len(scoreAry)-1-i][0])