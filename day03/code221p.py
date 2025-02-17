# 스택 응용

# 웹 서핑에서 이전 페이지 돌아가기
# URL 세곳을 방문한 후 약 5초 기다렸다가 다시 역순으로 방문하는 코드를 스택으로 구현

import webbrowser
import time

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
    urls = ['naver.com', 'daum.net', 'nate.com']

    for url in urls :
        push(url)
        webbrowser.open('https://'+url)
        print(url, end='-->')
        time.sleep(1)

    print("방문 종료")
    time.sleep(5)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('https://'+url)
        print(url, end='-->')
        time.sleep(1)
    print("방문 종료")