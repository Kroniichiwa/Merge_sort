a = [1,5,9,4,7,6,2,8,8,10,3,11]

def merge(a,b) :
    print("Sort : ",a, "with : ",b)
    i,j = 0,0
    result = []
    while i < len(a) and j < len(b) :
        if a[i] < b[j] :
            result.append(a[i])
            i+=1
        else :
            result.append(b[j])
            j+=1

    while i < len(a):
        result.append(a[i])
        i+=1

    while j < len(b):
        result.append(b[j])
        j+=1
    print("______________ Result is :", result,"\n")
    return result

def half_merge(L):
    print("List is : ", L)
    if len(L) < 2 :
        return L[:]
    else :
        middle = len(L) // 2
        left = half_merge(L[middle:])
        right = half_merge(L[:middle])
        return merge(left,right)


if __name__ == '__main__' :
    print(half_merge(a))