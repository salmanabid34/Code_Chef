def binary_search(list,item):
    low=0
    high=len(list)-1
    while low <= high:
        mid=round((low+high)/2)
        print (f'{low} + {high}' , end="\n")
        guess=(list[mid])
        if guess == item:
            return mid
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    return None       
List=[1,2,3,6,8,10,12]
print(binary_search(List,12))