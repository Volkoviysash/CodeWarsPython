n = 50
u = [1]
u2x = 0
u3x = 0
indx = 1

while indx <= n:
    u.append(min(2*u[u2x]+1, 3*u[u3x]+1))    
    if u[indx] == 2*u[u2x]+1: u2x+=1
    if u[indx] == 3*u[u3x]+1: u3x+=1    
    indx +=1

print("Un = ", u[n])
print("U = ", u)
