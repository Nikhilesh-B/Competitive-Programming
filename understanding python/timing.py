import time 

def billion_operations():
    for _ in range(10**5):
        print("Hello, World!")

start = time.time()
billion_operations()
end = time.time()

print(f"Time taken: {end - start} seconds")