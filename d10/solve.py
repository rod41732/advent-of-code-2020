from collections import defaultdict
nums = [int(e) for e in open('input.txt', 'r').readlines()]

nums.sort()
nums.append(max(nums)+3)

nums2 = [0] + nums[:-1]


cnt = defaultdict(int)

for a, b in zip(nums, nums2):
  cnt[a-b] += 1

print(cnt)
print(cnt[1] * cnt[3])