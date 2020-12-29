f = open('input.txt', 'r')
curTime = int(f.readline().strip())
bus = [int(e) for e in f.readline().strip().split(',') if e != 'x']

print(curTime)
print(bus)

def getTimeLeft(cur, interval):
  if cur % interval == 0:
    return 0
  return interval - cur % interval


x = [(getTimeLeft(curTime, busId), busId) for busId in bus]
minTime = min(x)

waitTime, busId = minTime
print(waitTime, busId)
print(waitTime * busId)