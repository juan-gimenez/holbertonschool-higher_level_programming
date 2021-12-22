def fizzbuzz():
    for int in range(1, 101):
        if int % 3 == 0 and int % 5 == 0:
            print("FizzBuzz ", end='')
            continue
        elif int % 3 == 0:
            print("Fizz ", end='')
            continue
        elif int % 5 == 0:
            print("Buzz ", end='')
            continue
        else:
            print("{:d} ".format(int), end='')
