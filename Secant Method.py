a = int(input("Enter Initial Value x0: "))
b = int(input("Enter Initial Value x1: "))
equation = input("Enter the equation: ")
f = lambda x: eval(equation)
ittr = int(input("Enter the no. of itterations: "))
for i in range(ittr):
    x = (b - ((f(b))*((b-a)/(f(b)-f(a))))) 
    a=b
    b=x
    print("itteration ",i," = ",x)



