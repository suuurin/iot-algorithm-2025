## 중복파일 이름 찾기
import os
from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right =None

# 전역변수
memory = []
root = None
fnameAry =[]

if __name__ == '__main__':
    folderName = 'C:/Program Files/Common Files/'
    for dirName, subDirLists, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)  # 파일명 전부 추가

    node = TreeNode()
    node.data = fnameAry[0]
    root = node
    memory.append(node)

    dupNameAry = []

    for name in fnameAry[1:]:
        node = TreeNode()
        node.data = name

        curr = root
        while True:
            if name == curr.data:
                dupNameAry.append(name)
                break
            if name < curr.data:
                if curr.left == None:
                    curr.left = node
                    memory.append(node)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.right = node
                    memory.append(node)
                    break
                else:
                    curr = curr.right
        
    # dupNameAry = list(set(dupNameAry))
    dupCounts = {}

    # print(list(dupNameAry))
    
    for file in list(dupNameAry):
        if file in dupCounts:
            dupCounts[file] += 1
        else:
            dupCounts[file] = 1

    duplicates = {file: count for file, count in dupCounts.items() if count >= 1}

    print(f'{folderName}, 및 하위 폴더의 중복된 파일 목록 -->')
    print(duplicates)