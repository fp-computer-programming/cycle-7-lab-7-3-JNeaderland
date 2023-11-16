#Author: Jacob Neaderland
#Adding all 4 options
gret1 = "Hello World!"
gret2 = "Hi World"
gret3 = "Hey World"
gret4 = "Hello World"
#Setting the 4 options
def greeting(gret):
    if gret == 1:
        print (gret1)
    elif gret == 2:
        print (gret2)
    elif gret == 3:
        print (gret3)
    elif gret == 4:
        print (gret4)
    else:
        print ("There's only 4 options!")
#Testing all 4 options
greeting(1)
greeting(2)
greeting(3)
greeting(4)

