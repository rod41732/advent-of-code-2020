from typing import Tuple
import re
import numpy as np
from collections import defaultdict
import heapq



instrs = open('input.txt', 'r').readlines()
N_INSTRS = len(instrs)
print(N_INSTRS, 'instructions')
OFFSET = N_INSTRS + 10

adj = defaultdict(list) 


# build two layer graph
for i, inst in enumerate(instrs):
  cmd, arg = inst.split()
  arg = int(arg)
  
  if cmd == 'acc':
    adj[i].append(i+1)
    adj[i+OFFSET].append(i+OFFSET+1)
  elif cmd == 'nop':
    adj[i].append(i+1)
    adj[i+OFFSET].append(i+OFFSET+1)
    # change to jump
    if 0 <= i + arg < N_INSTRS:
      adj[i].append(i+OFFSET+arg)
  elif cmd == 'jmp':
    adj[i].append(i+arg)
    adj[i+OFFSET].append(i+OFFSET+arg)
    # change to no-op
    if 0 <= i + arg < N_INSTRS:
      adj[i].append(i+OFFSET+1)


pq = []


N_NODES = N_INSTRS + OFFSET + 1
mindist = np.ones(N_NODES+1)*100000000
prev = {} # store path

# push (dist, node)
heapq.heappush(pq, (0, 0))
mindist[0] = 0
prev[0] = -1

while True:
  (dist, u) = heapq.heappop(pq)
  # print((dist, u))
  if u == N_INSTRS or u == N_INSTRS + OFFSET: 
    # print("Reached node", u)
    break
  if dist > mindist[u]:
    continue

  for v in adj[u]:
    if dist+1 < mindist[v]:
      mindist[v] = dist+1
      heapq.heappush(pq, (dist+1, v))
      prev[v] = u

p = u
while p != -1:
  if p >= OFFSET and prev[p] < OFFSET:
    print('should change instruction', prev[p], 'which is', instrs[prev[p]])
    break
  p = prev[p]

## output should change instruction 377 which is jmp +96
# now run solve2_part2.py
