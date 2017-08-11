#list=[0,1,2,3,4,5]
list=[0,1,1,2,3,5]
def fib(list):
    index=0
    for x in list:
        if x == 0:
            print (0)
            index=index+1
        elif x == 1:
            print(1)
            index= index+1
        else:
            print (list[index-2]+ list[index-1])
            index= index+1

fib(list)
