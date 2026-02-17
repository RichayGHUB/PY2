import time
def countdown(n):
    if n==0:
        print("HAPPY NEW YEAR!")
        return
    time.sleep(1)
    print(n)
    countdown(n-1)
countdown(5)

def factorialsum(f):
    if f==0:
        return 0
    return f+factorialsum(f-1)
print(factorialsum(5))

    