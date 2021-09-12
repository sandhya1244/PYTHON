marks = int(input("enter the marks\n"))
if marks>=90:
    grade="Ex"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B" 
elif marks>=50:
    grade="c"  
else:
    grade="f" 

print("your grade is" +  grade)     