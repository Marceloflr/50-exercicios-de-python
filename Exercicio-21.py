def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = 28
fahrenheit = 84

print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius):.2f}°F")
print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit):.2f}°C")
