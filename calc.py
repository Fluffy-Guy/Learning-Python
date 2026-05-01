num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
math = int(input("Enter the math type (+ is 1, - is 2, * is 3, / is 4)"))
if int(math) == 1:
 result = float(num1) + float(num2) 
elif int(math) == 2:
 result = float(num1) - float(num2) 
elif int(math) == 3:
 result = float(num1) * float(num2) 
elif int(math) == 4:
 result = float(num1) / float(num2)
print(f"Heres the result: {result}")
