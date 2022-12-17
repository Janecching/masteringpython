print([0]*5)                  #[0, 0, 0, 0, 0]
print([[0]*4 for i in range(4)])  #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# lst.pop()                   #O(1)
# lst.append(1)               #O(1)
# lst.insert(1,7)             #O(n)
# lst[-1]                     #O(1)
# lst[1:3]                    #start from 1 up to 3-1

a,b,c=[1,2,3]
print(a,b,c)                  #1,2,3

lst = [1,2,3]
for i,n in enumerate(lst): 
    lst[i] *=2                #2,4,6

nums1, nums2 = [1,2], [3,4]
for n1,n2 in zip(nums1, nums2): 
    print(n1,n2)              #1,3 \n 2,4

lst = ['a','b','c']
print(lst.sort(reverse=True)) # sorts in place, returns None, only works on list
print(lst)                    # lst is now sorted
lst = ['a','b','c']
print(sorted(lst)[::-1])      # creates sorted copy ['c','b','a'], can work on collections, sequences
print(lst)                    # lst is still not sorted
lst = ['a','apple','app']
lst.sort(key=lambda x:len(x)) # annonymous fn, arg: expression, sorts in place
print(lst)
print([i+i for i in range(3)]) #[0,2,4]

