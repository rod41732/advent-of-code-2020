nums = open('input1.txt', 'r').read().strip().split()
nums = list(map(int, nums))
n = len(nums)

pair = {}
# map sum -> array of (i, j); where nums[i] + nums[j] = sum
for i in range(n):
   for j in range(i+1, n):
      s = nums[i] + nums[j]
      if s not in pair: pair[s] = []
      pair[s].append((i,j))

found = False
for i, x in enumerate(nums):
   t = 2020-x
   if t in pair:
     for i1, i2 in pair[t]:
        if i != i1 and i != i2:
           print(nums[i]*nums[i1]*nums[i2])
           print(i, i1, i2, nums[i], nums[i1], nums[i2])
           found = True
           break
   if found: break


