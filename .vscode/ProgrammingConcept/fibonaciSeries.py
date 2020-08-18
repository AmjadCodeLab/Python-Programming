#print the fibonaci number present in a range using genrator concept

def fibonaci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

f=fibonaci()
for x in f:
    if x<100:
        print(x)