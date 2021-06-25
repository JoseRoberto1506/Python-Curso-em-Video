''' Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta 
pinta uma área de 2m².'''

wall_width = float(input("Largura da parede em metros: "))
wall_heigth = float(input("Altura da parede em metros: "))
area = wall_width * wall_heigth
ink = area / 2

print(f"Sua parede tem a dimensão de {wall_width}x{wall_heigth} e sua área é de {area}m².")
print(f"Para pintar essa parede, você precisará de {ink}L de tinta.")
