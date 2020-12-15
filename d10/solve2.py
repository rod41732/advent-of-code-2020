from collections import defaultdict
# nums = [int(e) for e in open('input-small1.txt', 'r').readlines()] # output = 8
# nums = [int(e) for e in open('input-small2.txt', 'r').readlines()] # output = 19208
nums = [int(e) for e in open('input.txt', 'r').readlines()] # output = 31581162962944

nums.sort()
nums = [0] + nums + [max(nums) + 3]

dp = [0] * len(nums)
dp[0] = 1

for i in range(1, len(nums)):
  for j in range(max(i-3, 0), i):
    if nums[i] - nums[j] <= 3:
      dp[i] += dp[j]

print(dp[-1])