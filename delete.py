



arr = [1,2,3,4,5,6,7]
d = 2
n = len(arr)
def rotate_left(arr,d,n):
    for i in range(d):
        rot_by_one(arr,n)
        print(arr)
        
def rot_by_one(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[0] = arr[i+1]

    arr[n-1] = temp
    # print(arr)




rotate_left(arr,d,n)
