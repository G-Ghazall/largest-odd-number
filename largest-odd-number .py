x,y,z=10,2,8
output=min(x,y,z)
if x%2 !=0:
    output = x
if y%2 !=0 and y>output:
    output = y
if z%2 !=0 and z>output:
    output = z
print (output)
