import random
Mem = 0
number = random.randint(1, 20)
print('Guess number 1-20')
while Mem < 5:
    print('Lets guess')
    A = input()
    if A.isdigit():
        
        A = int(A)                  
        Mem = Mem + 1

        if A < number:
            print('Too Low')
    
        if A > number:
            print('Too High')

        if A == number:
            break
    else:
        print('Input Number only')
        
if A == number:
    print('You win')

if A != number:
    print('You Lose The number is '+ str(number))
