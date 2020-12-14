import re
import numpy as np
data = [l.replace('contain', '|') for l in open('input.txt', 'r').readlines()]

# parsed conditions : word[ word] bags
conds = [re.findall('([a-z]+(?: [a-z]+)*) bags?', d) for d in data]
# print(conds[:5])

# generate color mapping
colors = set()
for c in conds:
  for color in c:
    colors.add(color)

colorMap = {}
for i, c in enumerate(colors):
  colorMap[c] = i

# generate adj matrix
n = len(colors)
arr = np.zeros((n,n))

for i in range(n):
  arr[i][i] = 1

for [outer, *rest] in conds:
  for inner in rest:
    arr[colorMap[outer]][colorMap[inner]] = 1

# find reachability 
for i in range(int(np.log2(n))+1):
  # arr = arr ** 2
  np.matmul(arr, arr, arr)
  arr[arr > 0] = 1

shinyGoldId = colorMap['shiny gold']
print('any -> shinyGold =', np.sum(arr[:, shinyGoldId]) - 1) # subtract shinyGold => shinyGold
