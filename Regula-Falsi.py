a = int(input("Enter Initial Value a: "))
b = int(input("Enter Initial Value b: "))
equation = input("Enter the equation: ")
f = lambda x: eval(equation)
ittr = int(input("Enter the no. of itterations: "))
for i in range(ittr):
    x  = ((a*f(b) - b*f(a))/(f(b)-f(a)))
    if f(x)<0:
        a = x
    else:
        b = x
    print("itteration ",i," = ",x)