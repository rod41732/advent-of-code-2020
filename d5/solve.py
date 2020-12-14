passes = open('input.txt', 'r').read().strip().split('\n')

def parse(passport: str) -> int:
  row = 0
  for c in passport[:7]:
    row = 2*row + (1 if c == 'B' else 0)
  col = 0
  for c in passport[7:]:
    col = 2*col + (1 if c == 'R' else 0)

  return row * 8 + col

passNum = [parse(passport) for passport in passes]
print("maxID", max(passNum))