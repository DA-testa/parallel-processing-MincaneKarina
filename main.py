# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    firstLine = input()
    # n - thread count 
    # m - job count
    
    a  = firstLine.split()
    n = int(a[0])
    m = int(a[1])
    #n = 0
    #m = 0
    print(n)
    print(m)

    # second line - data 
    secondLine = input()
    data = list(map(int, secondLine.split()))
    print(data)
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
