def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
results = []

for i in range(1, T + 1):
    ps = data[i]
    results.append(is_vps(ps))

for result in results:
    print(result)
