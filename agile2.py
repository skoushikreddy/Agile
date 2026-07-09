data = []
While True:
try: 
s = input()
if not s:
break
data.append(tuple(x.strip() for x 
in s.split(","))) 
except E0FError:
break
data.sort(key=lambda x: (x[0],
int(x[1]), int(x[2])))
print(data)