def fizzBuzz(num):
    for i in range(1, num + 1):
        if i % 15 == 0:
            print('Fizzbuzz')
        else:
            if i % 5 == 0:
                print('Buzz')
            else:
                if i % 3 == 0:
                    print('Fizz')
                else:
                    print(i)

        
fizzBuzz(100)
