#Take
lower = int(input("Enter a lower range :"))
upper = int(input("Enter a upper range :"))

print("Prime number between",lower, "and", upper, "are:")
#i
for num in range(lower, upper + 1):
    #all
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
           print(num)