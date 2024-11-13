gradelist=[]
passer=0
student_count=0
print (" Average Student Score")

while student_count < 5:
    x = float(input("Enter the student's Grade:"))
    if x <40 or x > 100:
        print("Invalid grade must be between 40 to 100 ")
    else:
        gradelist.append(x)
        student_count += 1
        if x >= 75:
            passer = passer + 1
            
            print("===============")
sum = sum (gradelist)
average = sum/len(gradelist)
percent_passer=passer/len(gradelist) * 100
print (f"Average Between All Students: {average:.2f}")
print (f"Passers: {passer}")
print (f"% of those who have passed: {percent_passer:.2f}%")
print (f"Grades: {gradelist}")
        
            
    
        