## This problem appeared in TCS Digital Exam | Elevate Wings 1 DCA Exam

#  Problem statement: A plane starts from a base and travels in any
#  directions for 1 minute each. The task is to find whether it returns
#  to same the base successfully or not. The input is given as string of
#  directions (eg: NNSEW)

dir_str = input()

def auto_pilot(str):

    # storing the directions in a list
    dir = []
    for i in range(len(str)):       
        dir.append(str[i])

    # counting the number of times the plane travelled to North and East directions
    # and comparing it to their counter direction respectively
    if dir.count('N') == dir.count('S') and dir.count('E') == dir.count('W'):
        return 'Returned Successfully'

    else:
        return 'Not Returned Successfully'

# driver code
print(auto_pilot(dir_str))