'''
File name - lnblist.py
● two lists are given below L1, L2.
● create a new list called L3 containing items in below given pattern
● From L1 it must take only odd index items
● From L2 it must take only even index items
'''
l1s=int(input("Enter the size of first list: "))
l1=[]
a=0
while a in range(0,l1s):
    ger=int(input("Enter the number for first list: "))
    l1.append(ger)
    a=a+1
print("The first list is: ",l1)
print()

l2s=int(input("Enter the size of second list: "))
l2=[]
b=0
while b in range(0,l2s):
    ger1=int(input("Enter the number for second list: "))
    l2.append(ger1)
    b=b+1
print("The second list is: ",l2)
print()

l3=[]
c=0
while c in range(0,l1s):
    if c%2 == 0:
        l3.insert(c,l2[c])
    else:
        l3.insert(c,l1[c])
    c=c+1

print("The final required lsit is: ",l3)