# Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF.

celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = ((celsius * 9) / 5) + 32

print(f"A temperatura de {celsius:.2f}°C corresponde a {fahrenheit:.2f}°F.")