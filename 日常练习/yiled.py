def fib_gen(limit):

    f0, f1 = 0, 1

    for n in range(limit):

        yield f0

        f0, f1 = f1, f0 + f1

 

if __name__ == "__main__":

    for x in fib_gen(10):

        print(x)