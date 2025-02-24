# p504 동적 계획법 응용
# 황금 미로에서 부자되기

def growRich():
    memo = [[0 for _ in range(col)] for _ in range(row)]
    memo[0][0] = goldMaze[0][0]

    rowSum = memo[0][0]
    for i in range(1, row):
        rowSum += goldMaze[0][i]
        memo[0][i] = rowSum

    colSum = memo[0][0]
    for i in range(1, col):
        colSum += goldMaze[i][0]
        memo[i][0] = colSum

    for r in range(1, row):
        for c in range(1, col):
            if (memo[r][c-1] > memo[r-1][c]):
                memo[r][c] = memo[r][c-1] + goldMaze[r][c]
            else:
                memo[r][c] = memo[r-1][c] + goldMaze[r][c]

    return memo[row-1][col-1]

## 전역 변수 선언 부분 ##
row, col = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
        [1, 3, 3, 0, 5],
        [1, 2, 4, 3, 0],
        [3, 3, 0, 4, 2],
        [1, 3, 4, 5, 3]]

## 메인 코드 부분 ##
macolGold = growRich()
print(f'황금 미로에서 얻은 최대 황금 개수 --> {macolGold}')



