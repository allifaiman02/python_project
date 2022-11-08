list = [2,3,4,5,6]
i= 0
sum = 0

#for i in range(0,len(list))  :
#   print("I is "+str(i))
#   sum += list[i]
#   print("Current sum is "+str(sum))
#   if i >= len(list) - 1  :
#      print("There is no more item")

while i < len(list)  :
    print("I is "+str(i))
    sum += list[i]
    i += 1
    print("Current sum is "+str(sum))

    if i > len(list)  :
        print("There is no more item")


print("Total number is "+str(sum))