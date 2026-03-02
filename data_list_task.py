id = [1,2,3,4]
Eng = [70,80,90,60]
Math = [90,90,80,80]
Computer = [80,80,90,90]
thistuple = ("apple", "banana", "cherry")

for i in range(len(id)):
    total = Eng[i]+Math[i]+Computer[i]
    average = total /3
    print(f"Student Id : {id[i]}")
    print(f"Total Number is : {total}")
    print(f"Average Number is : {average}")
    
    
print(len(thistuple))