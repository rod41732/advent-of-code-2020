import re
import numpy as np
from typing import Tuple
data = [l.replace('contain', '|') for l in open('input.txt', 'r').readlines()]

# parsed conditions
# returns like ['foo', '2 bar', '2 baz']
conds = [re.findall('((?:[0-9]+ )?[a-z]+(?: [a-z]+)+) bags?', d) for d in data]
print(conds[:5])

# '2 foo' -> (2, foo), 'no other' -> (0, 'other')
def splitColor(color: str) -> Tuple[int, str]:
  match = re.match('^(no|[0-9]+) (.*)$', color)
  if match is None:
    raise Exception("Invalid Pattern")
  num, color = match.groups()
  if num == 'no': num = 0
  else: num = int(num)
  return (num, color)
  

# generate color mapping (with some parsing)
colors = set()
for outer, *rest in conds:
  colors.add(outer)
  for inner in rest:
    _, color = splitColor(inner)
    colors.add(color)

colorMap = {}
for i, c in enumerate(colors):
  colorMap[c] = i

# generate matrix
n = len(colors)
arr = np.zeros((n,n))

# map condition to matrix
for [outer, *rest] in conds:
  for inner in rest:
    cnt, color = splitColor(inner)
    arr[colorMap[outer]][colorMap[color]] = max(arr[colorMap[outer]][colorMap[color]], cnt)


shinyGoldId = colorMap['shiny gold']

# number of bags when outer most bag is `colorId`, counting outer bag itself
def recur(colorId: int) -> int:
  ans = 1
  # loop over row colorId
  for (i, cnt) in enumerate(arr[colorId, :]):
    if cnt != 0:
      ans += cnt * recur(i)
  return ans

print(recur(shinyGoldId) - 1) # substract outer most bag (shiny gold itself)