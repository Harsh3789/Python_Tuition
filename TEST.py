f=int(input("The First No is : "))
s=int(input("The Second No is : "))
t=int(input("The Third No is : "))
fr=int(input("The Fourth No is : "))
fif=int(input("The Fifth No is : "))

if f==s and f==t and f==fr and f==fif:
    print("All No's are same")
if f>s and f>t and f>fr and f>fif:
    print("Fisrt No is the grsatest :",f)
if s>f and s>t and s>fr and s>fif:
    print("Second No is the greatest : ",s)
if t>f and t>s and t>fr and t>fif:
    print("Third No is the greatest : ",t)
if fr>f and fr>s and fr>t and fr>fif:
    print("Fourth No is the greatest : ",fr)
if fif>f and fif>s and fif>t and fif>fr:
    print("Fifth No is the greatest : ",fif)