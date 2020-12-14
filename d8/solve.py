from typing import Tuple
import re
import numpy as np

instrs = open('input.txt', 'r').readlines()

mark = np.zeros(len(instrs))

acc = 0
pc = 0

while True:
  if pc == len(instrs):
    print("Terminated")
    break
  if mark[pc] == 1:
    print("Infinite Loop")
    break

  mark[pc] = 1
  cmd, arg = instrs[pc].split()
  arg = int(arg)
  if cmd == 'acc':
    acc += arg
  elif cmd == 'nop':
    pass
  elif cmd == 'jmp':
    pc += arg
    continue

  pc += 1

print(acc)

