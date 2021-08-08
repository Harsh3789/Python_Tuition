Hindi=int(input("Enter the Marks of Hindi : "))
Eng=int(input("Enter the Marks of Eng : "))
Phy=int(input("Enter the Marks of Phy : "))
Chem=int(input("Enter the Marks of Chem : "))
Bio=int(input("Enter the Marks of Bio : "))

Total_Marks= 500
Students_marks=Hindi+Eng+Phy+Chem+Bio
Percentage=Students_marks/Total_Marks
if Percentage>=0.33:
    print("Pass")
if Percentage>=0.80:
    print("A")
if Percentage>=0.60 and Percentage<=0.79:
    print("B")
if Percentage>=0.40 and Percentage<=0.59:
    print("C")