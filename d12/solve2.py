# cmds = open('input-small.txt', 'r').readlines()
cmds = open('input.txt', 'r').readlines()
cmds = [
  (c[0], int(c[1:])) for c in cmds
]

# coord of ship
x, y = 0, 0
# coord of waypoint
wx, wy = 10, 1

# recursive version of rotate
# it rotate CCW 90 degree, n times
def rotate(x, y, n):
  if n == 0: return x, y
  return rotate(-y, x, n-1)


for c, arg in cmds:
  if c == 'N':
    wy += arg
  elif c == 'E':
    wx += arg
  elif c == 'S':
    wy -= arg
  elif c == 'W':
    wx -= arg
  elif c == 'L': # CCW 
    times = (arg//90%4+4)%4
    wx, wy = rotate(wx, wy, times)
  elif c == 'R': # CW, minus sign
    times = (-arg//90%4+4)%4
    wx, wy = rotate(wx, wy, times)
  elif c == 'F':
    x, y = x + wx*arg, y + wy*arg

print(x, y)
print(abs(x) + abs(y))

