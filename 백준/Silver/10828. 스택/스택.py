import sys

# 스택을 빈 리스트로 초기화
stack = []

# 입력의 수를 입력받음
n = int(sys.stdin.readline().strip())

# 명령어를 처리
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)