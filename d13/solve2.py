f = open('input.txt', 'r')
curTime = int(f.readline().strip())
bus = [int(e) for e in f.readline().strip().split(',') if e != 'x']

n = len(bus)


def gcd(a, b):
  if b == 0: return a
  return gcd(b, a%b)

for i in range(n):
  for j in range(i+1, n):
    if gcd(bus[i], bus[j]) != 1:
      raise "not pairwise coprime"

# OK, no exception thrown
lcm = 1
for b in bus: lcm *= b

# for each w_i waiting w_i time won't change remainder of other bus,
# but will change remainder of bus_i
waitIter = [
  (lcm//b) for b in bus
]

# total wait time, the answer
waitTime = 0
for i, b in enumerate(bus): # i is also remainder
  wt = waitIter[i]
  while True: # we would try at most bus_i time to find the solution
    waitTime += wt
    if waitTime % bus[i] == i:
      break

waitTime %= lcm
print(waitTime)
    



