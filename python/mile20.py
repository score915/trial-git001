def mile2meter(mile) :
    meter = mile * 1600
    return meter

distance = mile2meter(20)
print ("distance =" + str(distance))

distance = mile2meter(20, )
print (f"distance2 ={distance}")


distance = mile2meter(20, 10)
print ("distance =" + str(distance))
