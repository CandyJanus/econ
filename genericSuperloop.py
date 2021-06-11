while(superloop==1):
    x = int(input('Type the number of cycles you want to run.'))
    while x > 0:
        i+=1
        x-=1
        print('Cycle number ' + str(i) + ' is running.')