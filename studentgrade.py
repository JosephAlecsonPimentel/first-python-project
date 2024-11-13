name = input ("Enter your name:")
section = input ("Enter you section:")
PrelimGrade = float(input("Your grades this prelim:" ))  
MidtermGrade = float(input("Your grades this prelim:" ))  
FinalsGrade = float(input("Your grades this prelim:" ))  

if PrelimGrade > 100 or MidtermGrade > 100 or FinalsGrade > 100:
    print("input the grade from 60 to 100.")
    (exit)
elif PrelimGrade < 60 or MidtermGrade < 60 or FinalsGrade < 60:
    print ("input the grade from 60 to 100.")
    (exit)
else:
    FinalGrade = PrelimGrade * 0.3333 + MidtermGrade * 0.3333 + FinalsGrade * 0.3333
    FinalGraderound = round (FinalGrade)
    
    if FinalGraderound <= 100 and FinalGraderound >= 99:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 1.00, Excellent")
    elif FinalGraderound <= 100 and FinalGraderound >= 99:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 1.25, Outstanding")
    elif FinalGraderound <= 98 and FinalGraderound >= 96:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 1.50, Superior")  
    elif FinalGraderound <= 95 and FinalGraderound >= 93:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 1.75, Very Good")  
    elif FinalGraderound <= 92 and FinalGraderound >= 90:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 2.00, Good")
    elif FinalGraderound <= 89 and FinalGraderound >= 87:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 2.25, Satisfactory")
    elif FinalGraderound <= 86 and FinalGraderound >= 84:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 2.50, Fairy Satisfactory")
    elif FinalGraderound <= 83 and FinalGraderound >= 81:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 2.75, Fair") 
    elif FinalGraderound <= 80 and FinalGraderound >= 78:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 3.00, Passed")
    elif FinalGraderound <= 77 and FinalGraderound >= 76:
        print(f"Hello {name} from {section}!")
        print(f"Your Final Grade is {FinalGraderound}, and your GPA is 5.0, failed")
    
    
        
    
            