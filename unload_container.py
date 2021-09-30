## This problem appeared in TCS Digital Exam | TCS Elevate Wings 1 DCA Exam

#  Problem statement: Two robotic arms are used to unload chocolate boxes from
#  a container. Arm 1 can uload 1 box and arm 2 can unload 2 boxes at once.
#  Containers max capacity is 5000, arm 1 has max unload capacity of 2500
#  and arm 2 has max unload capacity of 5000. Find the possible quantity 
#  of chocolate boxes in the container such that both arms start and end
#  unloading simulataneously and the container is unloaded completely.

#  Example Input: 100,200
#  Output: Yes (because arm 1 can unload 100 boxes (which is less than
#  2500) in the same time arm 2 takes to unload 200 boxes (which is
#  less than 5000), also total boxes in the container is 300 which
#  is less than 5000)

def checkUnload(x, y):
    
    # condition checking all the given conditions
    if x > 0 and x <= 2500 and y > 0 and y <= 5000 and x+y <= 5000 and y == 2*x:
        return True
    else:
        return False

# driver code
if __name__ == '__main__':
	
    # taking two inputs from user
    x, y = input().split(',')

    if checkUnload(int(x), int(y)):
        print("Yes")
    else:
        print("No")