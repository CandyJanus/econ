PREY_BIRTH_DEATH_MODIFIER=1
CARRY_CAP=1000
INVERSE_CARRY_CAP=1/CARRY_CAP
PREDATION_MODIFIER=0.01
FOOD_VALUE=0.0001
PREDATOR_BIRTH_DEATH_MODIFIER=0.01

EULER_STEP_LENGTH = 0.1

class Model:
    def __init__(self, initial_r=0, initial_f=0):
        self.r = initial_r # number of rabbits
        self.f = initial_f # number of foxes

    def execute_single_iteration(self):
        dr=PREY_BIRTH_DEATH_MODIFIER*self.r*(1-INVERSE_CARRY_CAP*self.r)-PREDATION_MODIFIER*self.r*self.f
        df=PREDATION_MODIFIER*self.r*self.f-PREDATOR_BIRTH_DEATH_MODIFIER*self.f

        dr=dr*EULER_STEP_LENGTH
        df=df*EULER_STEP_LENGTH

        self.r += dr
        self.f+=df

        if (self.r<0):
            self.r=0
        
        if (self.f<0):
            self.f=0

    def __str__(self):
        return 'There are '+ str(round(self.r))+' rabbits. and ' + str(round(self.f))+' foxes.'



if __name__ == "__main__":

    M = Model(10, 1)
    i=0
    # while(True):
        # x = int(input('Type the number of cycles you want to run.'))
    NUM_ITERATIONS = 3
    while i < NUM_ITERATIONS:
        i+=1
        print('Cycle number ' + str(i) + ' is running. \n')
        M.execute_single_iteration()