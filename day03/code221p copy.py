# 스택 응용

# 헨젤과 그레텔의 집으로 돌아가기
# 돌을 떨어뜨리면서 숲으로 돌아간다. 과자집에서집으로 돌아갈 때는 떨어뜨린순서와 반대로 돌을 주워야 한다.

import random

## 함수 선언 부분 ##
# da03_stack과 동일
def isStackFull(): # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if (top == SIZE - 1): # Full / 실무에서 쓰는 스택은 거의 무제한
        return True
    else: 
        return False
    
def isStackEmpty(): # 스택이 비었는지 확인
    global SIZE, stack, top
    if (top == -1): # Empty
        return True
    else:
        return False
    
def push(data): # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull(): # isStackFull() == True와 동일
        print('Stack is Full')
        # return 생략
    else:
        top += 1
        stack[top] = data

def pop(): # 스택에서 데이터 추출
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty.')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek(): # 스택의 top 위치의 데이터 확인(살짝보기)
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty.')
        return None
    else:
        return stack[top]
    
#=======================================================
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1
#=======================================================

## 메인 코드 부분 ##
if __name__ == "__main__":
    stoneAry = ["빨강", "파랑", "초록", "노랑", "보라", "주황"]
    random.shuffle(stoneAry)

    print("과자집에 가는길 : ", end=' ')
    for stone in stoneAry :
        push(stone)
        print(stone, "-->", end=' ')
    print("과자집")

    print("우리집에 오는길 : ", end=' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, "-->", end=' ')
    print("우리집")