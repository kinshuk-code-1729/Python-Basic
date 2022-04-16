import time
start=time.time()
r=0
for i in range(400):
    for n in range(400):
        r=r+(i*n)
print(r)
end=time.time()
print(end - start)
