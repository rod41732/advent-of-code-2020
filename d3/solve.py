map = [line.strip() for line in open('input.txt', 'r').readlines()]
col = len(map[0]) 
row = len(map) 
tree = sum(1 for i in range(row) if map[i][i*3%col] == '#')
print(tree)
