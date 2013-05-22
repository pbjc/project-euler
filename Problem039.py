#===============================================================================
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p <= 1000, is the number of solutions maximised?
#===============================================================================

high = 0
highval = 0
for p in range(1001):
    solutions = 0
    for a in range(1, p // 2):
        for b in range(1, a):
            c = (a * a + b * b) ** .5
            if a + b + c == p:
                solutions += 1
    if solutions > high:
        high = solutions
        highval = p
print(highval)