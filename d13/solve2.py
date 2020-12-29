f = open('input.txt', 'r')
curTime = int(f.readline().strip())
# pair of bus id, sequence
bus = [(int(e), i) for (i, e) in enumerate(f.readline().strip().split(',')) if e != 'x']

n = len(bus)


def gcd(a, b):
  if b == 0: return a
  return gcd(b, a%b)


# check precondition before using our algorithm
for i in range(n):
  for j in range(i+1, n):
    if gcd(bus[i][0], bus[j][0]) != 1:
      raise "not pairwise coprime"

# OK, no exception thrown
lcm = 1
for (b, _) in bus: lcm *= b

# for each w_i waiting w_i time won't change remainder of other bus,
# but will change remainder of bus_i
waitIter = [
  (lcm//b) for (b, i) in bus
]

# total wait time, the answer
waitTime = 0
for i, (b, timeLeft) in enumerate(bus): # i is also remainder
  wt = waitIter[i]
  while True: # we would try at most bus_i time to find the solution
    waitTime += wt
    if (waitTime + timeLeft) % b == 0:
      break

waitTime %= lcm
print(waitTime)
    



