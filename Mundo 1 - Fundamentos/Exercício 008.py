# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

meters = float(input("Digite uma distância em metros: "))
km = meters / 1000
hm = meters / 100
dam = meters / 10
dm = meters * 10
cm = meters * 100
mm = meters * 1000

print(f"A medida de {meters}m corresponde a:")
print(f"{km} km\n{hm} hm\n{dam} dam\n{dm} dm\n{cm} cm\n{mm} mm")