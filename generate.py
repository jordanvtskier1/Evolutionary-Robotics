import pyrosim.pyrosim as pyrosim


pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x=-3
y=-3
z=.5

i = 1
s = 1


while x<2:
    x+=1
    y=-3
    while y<2:
        while z <10:
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length/s,width/s,height/s])
            z+=1
            s+=.1
            i+=1
        y+=1
        s=1
        z=.5
    
#pyrosim.Send_Cube(name="Box2", pos=[1,y,1.5] , size=[length,width,height])


pyrosim.End()
