# 선택 정렬과 퀵 정렬의 성능 비교
# 선택 정렬은 개수가 많아질 수록 시간이 급격히 증가, 퀵 정렬은 개수가 많아져도 시간이 비슷하게 증가(빠르게 정렬 가능)

import random
import time

## 클래스와 함수 선언 부분 ##
def selectoinSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

def qSort(arr, start, end):
    if end <= start:
        return
    low = start
    high = end

    pivot = arr[(low + high) // 2] # 작은값은 왼쪽, 큰값은 오른쪽으로 분리
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)

## 메인 코드 부분 ##
countAry = [1000, 10000, 12000, 15000]

for count in countAry :
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'## 데이터 수 : {count}')
    start = time.time()
    selectoinSort(selectAry)
    end = time.time()
    print('선택 정렬 --> %10.3f 초' % (end-start))
    start = time.time()
    quickSort(quickAry)
    end = time.time()
    print('  퀵 정렬 --> %10.3f 초' % (end-start))
    print()

    count *= 5