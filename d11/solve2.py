from itertools import product
# board = open('input-small.txt', 'r').readlines()
board = open('input.txt', 'r').readlines()

b = [[1 if seat == 'L' else 0 for seat in row.strip()] for row in board]
b2 = [[1 if seat == 'L' else 0 for seat in row.strip()] for row in board]

r = len(b)
c = len(b[0])


# memoization
memo = {}
dir = [(dx, dy) for dx, dy in product([-1, 0, 1], [-1, 0, 1]) if dx != 0 or dy != 0]
assert len(dir) == 8

def getAdj(i, j):
  if (i, j) in memo:
    return memo[(i, j)]

  adjs = []

  for dx, dy in dir:
    for t in range(1, 100):
      nx, ny = i + dx*t, j + dy*t
      # out of bound check
      if not (0 <= nx < r and 0 <= ny < c):
        break
      # not floor
      if b[nx][ny] != 0:
        adjs.append((nx, ny))
        break
  
  memo[(i, j)] = adjs
  return adjs
  
  


def iter(b, b2):
  for i in range(r):
    for j in range(c):
      adjs = getAdj(i, j)
      occ = sum(1 for ii, jj in adjs if b[ii][jj] == 2)
      if b[i][j] == 1:
        b2[i][j] = 2 if occ == 0 else 1
      elif b[i][j] == 2:
        b2[i][j] = 1 if occ >= 5 else 2
      else:
        b2[i][j] = 0
  return b2 != b


def show(board):
  for row in board:
    print(''.join('.L#'[seat] for seat in row))
  print("="*10)
  print('')

def count(board):
  return sum(
    sum(1 for seat in row if seat == 2) for row in board
  )

show(b2)

while iter(b, b2):
  show(b2)
  (b, b2) = (b2, b)

show(b2)

print(count(b2))

