import random

def ran_gen(n): #Generates n random points
    if n >0:
        return[(random.randint(1,100), random.randint(1,100)) for i in range(n)]
    else:
        return None

def stair_recurrence(points): #Recurrence function to divide and conquer

    if(len(points)==1):
        return points
    
    sorted_pts = sorted(points, key=lambda p:(p[1],p[0]), reverse=True)
    
    mid = len(sorted_pts)//2

    left_half = stair_recurrence(sorted_pts[:mid])
    right_half = stair_recurrence(sorted_pts[mid:])

    return stair_merge(left_half, right_half)

def stair_merge(staircase1, staircase2): #function to merge
    merged_staircase = []
    i,j = 0,0

    while i<len(staircase1) and j<len(staircase2):
        if staircase1[i][1] < staircase2[j][1]:
            merged_staircase.append(staircase1[i])
            i+=1
        else:
            merged_staircase.append(staircase2[j])
            j+=1
    
    merged_staircase.extend(staircase1[i:])
    merged_staircase.extend(staircase2[j:])

    return merged_staircase
    

n = int(input("Enter the value of n:"))
points = ran_gen(n)

if(points == None):
    print("Invalid input")
else:
    result = stair_recurrence(points)
    print(result)