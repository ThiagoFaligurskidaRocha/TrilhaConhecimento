def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print("Escolha uma opção de conversão:")
print("[1]. Fahrenheit -> Kelvin")
print("[2]. Kelvin -> Celsius")
print("[3]. Celsius -> Fahrenheit")

opcao = int(input("Digite o número da opção: "))

if opcao == 1:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    kelvin = fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit} Fahrenheit equivale a {kelvin:.2f} Kelvin")
elif opcao == 2:
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    celsius = kelvin_to_celsius(kelvin)
    print(f"{kelvin} Kelvin equivale a {celsius:.2f} Celsius")
elif opcao == 3:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius equivale a {fahrenheit:.2f} Fahrenheit")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1 (Fahrenheit -> Kelvin), 2 (Kelvin -> Celsius) ou 3 (Celsius -> Fahrenheit) ).")
    
    
