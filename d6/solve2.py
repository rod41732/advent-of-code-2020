import re
import string
groups = open('input.txt', 'r').read().strip().split('\n\n') # split by blank lines

def countGroup(groupLines: str) -> int:
  answers = [set(person) for person in groupLines.strip().split('\n')]
  
  return sum(1 for c in string.ascii_lowercase \
      if all(c in ans for ans in answers)
  )

groupCount = [countGroup(group) for group in groups]
print(sum(groupCount))