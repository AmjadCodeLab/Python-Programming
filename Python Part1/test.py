l =(x*x for x in range(100000000000000000000000000000000000))
print(l)


from threading import *
import time

def sqaure(numbers):
    for n in numbers:
        print("Squares : ",n*n)

def double(numbers):
    for n in numbers:
        print("Double : ",2*n)

numbers=[1,2,3,4,5,6]
beigntime = time.time()
t1=Thread(target=sqaure,args=(numbers,))
t2=Thread(target=double,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime = time.time()
print("Total time taken :: " , endtime-beigntime)