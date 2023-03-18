# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    a = []
    for i in range(int(n)):
        a.append(i)
            
    threads  = []
    index = 0
    for i in range(int(m)+1):
        if index > n-1:
            index = 0
        threads.append(a[index])
        index = index +1
            
    
    t = []
    for i in range(n):
        t.append(0)
    
    for i in range(m):
       
       thread = threads[i]
       time = t[thread]

       output.append([thread, time])
       t[thread]= time  + data[i]
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

    # second line - data 
    secondLine = input()
    data = list(map(int, secondLine.split()))
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
