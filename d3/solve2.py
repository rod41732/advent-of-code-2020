map = [line.strip() for line in open('input.txt', 'r').readlines()]
col = len(map[0]) 
row = len(map) 
t1 = sum(1 for i in range(row) if map[i][i%col] == '#')
t2 = sum(1 for i in range(row) if map[i][i*3%col] == '#')
t3 = sum(1 for i in range(row) if map[i][i*5%col] == '#')
t4 = sum(1 for i in range(row) if map[i][i*7%col] == '#')
t5 = sum(1 for i in range(0, row, 2) if map[i][i//2%col] == '#')
print(t1*t2*t3*t4*t5)
