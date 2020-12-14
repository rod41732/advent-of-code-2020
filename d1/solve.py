nums = open('input1.txt', 'r').read().strip().split()
nums = list(map(int, nums))
s = set()
for n in nums:
   if 2020 - n in nums:
      print(n * (2020-n))
      break
   else:
      s.add(n)

