import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
print("\nAddition       =", proxy.add(a, b))
print("Subtraction    =", proxy.subtract(a, b))
print("Multiplication =", proxy.multiply(a, b))
print("Division       =", proxy.divide(a, b))
