def TowerOfHanoi(n , source, Temp,destination):
    global a
    if n==1:
        a+=1
        print ("Step :",a,": Move disk 1 from ",source,"------>",destination)
        return
    TowerOfHanoi(n-1, source, destination, Temp)
    a+=1
    print ("Step :",a,": Move disk",n,"from ",source,"------>",destination)
    TowerOfHanoi(n-1, Temp, source, destination)
a=0          
n = int(input("Enter number of disks :"))
print("   |   |   |")
print("   |   |   |")
print("   |   |   |")
print("``````````````")
print("   a   b   c\n\n")
TowerOfHanoi(n,'a','b','c')
print ("\nSolved :- )  ")

