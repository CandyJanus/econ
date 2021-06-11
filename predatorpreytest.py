#predatorpreyasshole


#starting values
R=10
F=1

preybirthdeathmodifier=1
carrycap=1000
inversecarrycap=1/carrycap
predationmodifier=0.01
foodvalue=0.0001
predatorbirthdeathmodifier=0.01

i=0
superloop=1

print('Cycle number 1 is running.')
print('There are '+ str(R)+' rabbits.')     
print('There are '+ str(F)+' foxes.')   

#superloop
while(superloop==1):

    x = int(input('Type the number of cycles you want to run.'))
    while x > 0:
        i+=1
        x-=1
        print('Cycle number ' + str(i) + ' is running.')
        dR=preybirthdeathmodifier*R*(1-inversecarrycap*R)-predationmodifier*R*F
        
        dF=predationmodifier*R*F-predatorbirthdeathmodifier*F
        
        #literally just a scaling factor to make the simulation more stable
        #lol rabbits still go extincterinos
        dR=dR*0.01
        dF=dF*0.01

        R=R+dR
        if (R<0):
            R=0
        print('There are '+ str(R)+' rabbits.')      

        F=F+dF
        if (F<0):
            F=0
        print('There are '+ str(F)+' foxes.')