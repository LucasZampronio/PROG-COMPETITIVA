import time
x = int(input())
start_time = time.time()
for m in range(x, 0 ,-1):
    bina = bin(m)[2:]
    if bina == bina [::-1]:
        print(m)
        break
execution_time = time.time() - start_time
print(f"Execution time: {execution_time} seconds")
