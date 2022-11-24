employee = {}

max_length = 1

while len(employee) < max_length :
    name = input("Enter employee's name : ")
    #salary = int(input("Enter employee's salary : "))
    
    work_exp = []
    for j in range (3) :
        work = input("Enter your work experince No " + str(j+1) + " :")
        work_exp.append(work) 


    if name not in employee :
        #employee[name] = salary
        employee[name] = work_exp

print(employee)