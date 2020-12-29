# cmds = open('input-small.txt', 'r').readlines()
cmds = open('input.txt', 'r').readlines()
cmds = [
  (c[0], int(c[1:])) for c in cmds
]


# north east south west
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
currentDir = 1

x, y = 0, 0

for c, arg in cmds:
  if c == 'N':
    y += arg
  elif c == 'E':
    x += arg
  elif c == 'S':
    y -= arg
  elif c == 'W':
    x -= arg
  elif c == 'L':
    currentDir = (currentDir-(arg//90%4)+4)%4
  elif c == 'R':
    currentDir = (currentDir+(arg//90%4)+4)%4
  elif c == 'F':
    dx, dy = dirs[currentDir]
    x, y = x + dx*arg, y + dy*arg

print(x, y)
print(abs(x) + abs(y))

