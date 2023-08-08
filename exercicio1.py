import random

#Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo dele é
#acertar a palavra em no máximo 5 tentativas. Informe sempre quantas tentativas ele
#ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (de
#preferência não fixa). Ao final, mostre a palavra correta e o número de tentativas que
#ele utilizou.

frutas = ['maça', 'pera', 'uva', 'banana', 'abacaxi', 'limão', 'laranja', 'abacate', 'amora']
random.shuffle(frutas)
certa = 'maça'
contador = 5

for i in range(1, contador + 1):
    print(f"A lista de frutas possui 9 elementos. Tente acertar o elemento escolhido com cinco tentativas.")
    tent_palavra = str(input("Informe uma fruta: "))

    if tent_palavra == certa:
        print("Correto! Você acertou.")
        break
    else:
        print(f"Tente novamente, você possui ainda {contador - i} tentativas.")

if i == contador and tent_palavra != certa:
    print(f"Suas tentativas acabaram. A fruta correta era {certa}")
