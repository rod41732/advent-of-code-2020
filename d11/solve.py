from itertools import product
# board = open('input-small.txt', 'r').readlines()
board = open('input.txt', 'r').readlines()

b = [[1 if seat == 'L' else 0 for seat in row.strip()] for row in board]
b2 = [[1 if seat == 'L' else 0 for seat in row.strip()] for row in board]

r = len(b)
c = len(b[0])


def iter(b, b2):
  for i in range(r):
    for j in range(c):
      adjs = product(
        range(max(i-1, 0), min(i+2, r)),
        range(max(j-1, 0), min(j+2, c))
      )
      occ = sum(1 for ii, jj in adjs if (ii != i or jj != j) and b[ii][jj] == 2)
      if b[i][j] == 1:
        b2[i][j] = 2 if occ == 0 else 1
      elif b[i][j] == 2:
        b2[i][j] = 1 if occ >= 4 else 2
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

