import re
groups = open('input.txt', 'r').read().strip().split('\n\n') # split by blank lines

def countGroup(groupLines: str) -> int:
  return len(set(re.sub('\n', '', groupLines)))

groupCount = [countGroup(group) for group in groups]
print(sum(groupCount))