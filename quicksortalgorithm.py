def qs(arr,low,high): #quicksort algorithm
    if(low>=high):
        return
    pindex=getpindex(arr,low,high)
    qs(arr,low,pindex-1)
    qs(arr,pindex+1,high)
def getpindex(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<high):
            i+=1
        while(arr[j]>=pivot and j>low):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[low]=arr[low],arr[j]
    return j
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
qs(arr,low,high)
print(arr)
    
