arr=[3,1,7,5,10,8,21,12]
arr=list(map(int,input("Enter the array : ").split()))
a=len(arr)
for i in range(0,a-1): #how many time runes
    for j in range(0,len(arr)-1): # swap the values
        if arr[j] < arr[j+1]:
            continue
        elif arr[j] > arr[j+1]: 
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)











