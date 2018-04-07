
def TroubleSort(L,sz):
    done = False
    while not done:
        done = True
        for i in xrange(0,sz-2):
            if L[i] > L[i+2]:

                done = False
                L[i],L[i+2] = L[i+2],L[i]
    #             temp = L[i]
    #             L[i] = L[i+2]
    #             L[i+2] = temp
    #print(L)

n = int(raw_input())  # test cases
#print "N :" + str(n)
for i in xrange(0,n):
    sz = int(raw_input()) # size of case WE DONT NEED IT SO FAR
    input = raw_input().split()
    input = [int(x) for x in input]
    #print "Input is " + str(input)
    sorted = True
    TroubleSort(input,sz)

    for x in xrange(0,sz-1):
        if input[x] > input[x+1]:
            print "Case #" + str(i + 1) + ": {}".format(x)
            sorted = False
            break
    if sorted:
        print "Case #" + str(i + 1) + ": OK"






