x, y, z = int(input()), int(input()), int(input())
if x<y: x, y = y, x
if y<z: y, z = z, y
if x<y: x, y = y, x
print(str(x) + '\n' + str(z) + '\n' + str(y))
