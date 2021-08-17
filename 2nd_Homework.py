# 1. Write a Python program to find the largest number among the five input numbers using elif

first=int(input("Enter the First No : "))
second=int(input("Enter the second No : "))
third=int(input("Enter the third No : "))
fourth=int(input("Enter the fourth No : "))
fifth=int(input("Enter the fifth No : "))

if first>second and first>third and first>fourth and first>fifth:
    print("First No is the largest No :",first)
elif second>first and second>third and second>fourth and second>fifth:
    print("Second No is the largest No :",second)
elif third>first and third>second and third>fourth and third>fifth:
    print("Third No is the largest No :",third)
elif fourth>first and fourth>second and fourth>third and fourth>fifth:
    print("Fourth No is the largest No :",fourth)
elif fifth>first and fifth>second and fifth>third and fifth>fourth:
    print("Fifth No is the largest No :",fifth)



first=int(input("Enter the First No : "))
second=int(input("Enter the second No : "))
third=int(input("Enter the third No : "))
fourth=int(input("Enter the fourth No : "))
fifth=int(input("Enter the fifth No : "))

if first>second and first>third and first>fourth and first>fifth:
    print("First No is the largest No :",first)
elif second>first and second>third and second>fourth and second>fifth:
    print("Second No is the largest No :",second)
elif third>first and third>second and third>fourth and third>fifth:
    print("Third No is the largest No :",third)
elif fourth>first and fourth>second and fourth>third and fourth>fifth:
    print("Fourth No is the largest No :",fourth)
else:
    print("Fifth No is the largest No :",fifth)


# 2. Write a python program input any charactor and Check Whether a Character is a Vowel or Consonant
vowel=["a","e","i","o","u"]
char=input("Enter a character : ")
if char in vowel:
    print("The Entered character is vowel :",char)
else:
    print("The Entered character is consonant :",char)