arr1 = input("Enter numbers: ")   
l1 = list(map(int,arr1.split(' ')))

arr2 = input("Enter numbers: ")  
l2 = list(map(int,arr2.split(' ')))

print("Common elements: ", set(l1).intersection(l2))
print("All elements: ", set(l1).union(l2))
