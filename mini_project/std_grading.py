ds=float(input("Enter marks in discrete structure: "))
mth=float(input("Enter marks in mathematics-II : "))
oop=float(input("Enter marks in OOPS : "))
mp=float(input("Enter marks in micro processor: "))
st=float(input("Enter marks in statistics : "))

def calculateGpa(m):
    if m>=90:
        return 4.0
    elif m<90 and m>=80:
        return 3.7
    elif m<80 and m>=70:
        return 3.3
    elif m<70 and m>=60:
        return 3.0
    elif m<60 and m>=50:
        return 2.7

    else:
        return 0
    
gp_of_ds=calculateGpa(ds)*3
gp_of_math=calculateGpa(mth)*3
gp_of_oop=calculateGpa(oop)*3
gp_of_stat=calculateGpa(st)*3
gp_of_mp=calculateGpa(mp)*3
print("\n")
CGPA=(float)(gp_of_ds+gp_of_math+gp_of_mp+gp_of_oop+gp_of_stat)/15
if CGPA==0:
    print("You have failed: ")
else:
    
    print("-------------------------------------RESULT-------------------------------------\n")
    print(f"{"Subjects":<19}\t\t\t{"Credit Hours":^12}\t\t\t{"GPA":-^5}")
    print(f"{"Discrete Structure":<19}\t\t\t{"3":^12}\t\t\t{gp_of_ds:>5.2f}")
    print(f"{"Mathematics-II":<19}\t\t\t{"3":^12}\t\t\t{gp_of_math:>5.2f}")
    print(f"{"OOP":<19}\t\t\t{"3":^12}\t\t\t{gp_of_oop:>5.2f}")
    print(f"{"Statistics-I":<19}\t\t\t{"3":^12}\t\t\t{gp_of_stat:>5.2f}")
    print(f"{"Micro Processor":<19}\t\t\t{"3":^12}\t\t\t{gp_of_mp:>5.2f}")

    print(f"\nYour CGPA is {CGPA:.2f}")
