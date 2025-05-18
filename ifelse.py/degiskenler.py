for a in range(10):
    b = 4 
    print(b)

c=2
def a():
    global c 
    c = 5
a()
print(b*2)
print(c*2)