# Temperature Converter: Celsius <-> Fahrenheit

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

print("Temperature Converter")
choice = input("Convert from (C)elsius or (F)ahrenheit? ").lower()

if choice == "c":
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", c_to_f(c))
elif choice == "f":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", f_to_c(f))
else:
    print("Invalid choice")
