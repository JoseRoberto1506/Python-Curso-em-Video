''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: 
IMC abaixo de 18,5: Abaixo do Peso. 
Entre 18,5 e 25: Peso Ideal. 
25 até 30: Sobrepeso. 30 até 40: 
Obesidade. 
Acima de 40: Obesidade Mórbida.'''

weigth = float(input("Qual é seu peso? (Kg) "))
heigth = float(input("Qual é sua altura? (m) "))
IMC = weigth / (heigth ** 2)

print(f"O seu IMC é de {IMC:.1f}.")

if IMC < 18.5:
    print("Você está abaixo do peso.")
elif IMC < 25:
    print("PARABÉNS, você está na faixa de peso ideal.")
elif IMC < 30:
    print("Você está na faixa de sobrepeso.")
elif IMC < 40:
    print("Você está em OBESIDADE!")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")
