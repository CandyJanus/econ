#import scipy
#having troubles integrating scipy

#Simple Prisoners Dilemma Matrix

#           | DEFECT | COOPERATE
# DEFECT    | 0          10
# COOPERATE | 10         5

pdMat=[[0, 10],[10,5]]

class AbstractDecisionAgent:
    utilityStored = 0
    
class alwaysDefect(AbstractDecisionAgent):
    decisionMatrix=[1,0]
class alwaysCooperate(AbstractDecisionAgent):
    decisionMatrix=[0,1]

numPlayers=2
percent_alwaysdefect=50
percent_alwayscooperate=50

num_alwaysdefect=int(numPlayers*percent_alwaysdefect/100)
num_alwayscooperate=int(numPlayers*percent_alwayscooperate/100)

if(num_alwayscooperate+num_alwaysdefect!=numPlayers):
    raise Exception("Not all players correctly assigned strategy, does not sum to numPlayers.")
 
#I'm doing this in the most cancer way, it will not scale up to 
#an arbitrary number of player types.
 
playerList=[]
for i in range (num_alwaysdefect):
    playerList.append(alwaysDefect)
for i in range (num_alwayscooperate):
    playerList.append(alwaysCooperate)

#I'm going to look up how other people implement PD lol

print('Cycle number 1 is running.')

while(superloop==1):
    x = int(input('Type the number of cycles you want to run.'))
    while x > 0:
        i+=1
        x-=1
        print('Cycle number ' + str(i) + ' is running.')
        for all x in playerList:
            for all y in playerList:
                pDCalc(x,y)
        
        
#You know, I think and I dream. What makes people, people, is
#their ability to hold histories and grudges. It's why crows
#are more people than ecoli. I have not yet implemented a sense
#for history in my agents, nor for forgiveness.      
        
   
# def pDCalc(Agent1, Agent2):
    # Agent1.decisionMatrix()
    # Agent2.decisionMatrix()
    

        
#Reward Matrix

#         | LOOT | PRODUCE
# LOOT    |
# PRODUCE |
