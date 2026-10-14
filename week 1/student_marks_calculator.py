print("===== STUDENT MARKS CALCULATOR =====")
name= input("enter the student name:")
maths=int(input("enter the maths marks"))
chemistry=int(input("enter the chemistry marks"))
physics=int(input("enter physics marks"))
marks = maths+chemistry+physics
print("you are doing great",name.upper())
print("your total marks is :",marks)
percentage=marks/300*100
print("your total percentage is :",percentage,"%")
print("\n" + "=" * 36)


