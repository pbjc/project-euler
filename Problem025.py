#===============================================================================
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#===============================================================================

a, b, term = 0, 1, 0
while True:
    term += 1
    if len(str(b)) == 1000:
        break
    b += a
    a = b - a
print(term)