import time

def timef():
    t = time.strftime("%b %d, %H:%M:%S")
    return (t)
print(f"It is {timef()}")