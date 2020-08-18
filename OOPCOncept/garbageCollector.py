import time
import sys
class Test:
    def __init__(self):
        print("Object Identification...")

    def __del__(self):
        print("Object Termination Or CleanUp...")

t1=Test()
#t1=None
t2=t1
t3=t2
print(sys.getrefcount(t1))  #to find the number of reference of an object
del t1
time.sleep(5)
print("Object not Yet Deleted after t1 delete")

del t2
time.sleep(5)
print("Object not Yet Deleted after t2 delete")

del t3
print("Object Clean Up to process as t3 deleted")
time.sleep(5)
print("End of Application")

