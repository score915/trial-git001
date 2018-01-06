import bisect
import datetime
import time

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#    print("Score=" + str(score))
    i = bisect.bisect(breakpoints, score)
#    print("i=" + str(i))
    return grades[i]

grade(score = 33)

print( [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
#time.sleep(2.0)
#print( [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
#time.sleep(2.0)
#print( [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
#time.sleep(2.0)

#print(datetime.strftime("%x"))
print(time.strftime("%x"))

# grade(score) for score in [33, 99, 77, 70, 89, 90, 100]
