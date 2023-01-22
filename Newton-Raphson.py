from sympy import symbols, diff
x = symbols('x')
a = int(input("Enter Initial Value x: "))
equation = input("Enter the equation: ")
f = lambda x: eval(equation)
f1 =str(diff(eval(equation), x))
f_ = lambda x: eval(f1)
print(f_(a))
ittr = int(input("Enter the no. of itterations: "))
for i in range(ittr):
    x = (a - (f(a)/f_(a))) 
    a=x
    print("itteration ",i," = ",x)