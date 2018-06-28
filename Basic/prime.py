import time

def isPrime(num):
    if num == 1 or num == 2 or num == 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

count = 0
print("PRIME NUMBERS BETWEEN 1 AND 500 :")
start = time.time();
for i in range(1, 500):
    if isPrime(i):
        count+=1
print("\nTOTAL : ",count)
end = time.time();
print("\nTIME : ",(end-start)," seconds")