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

#Incluir escolha de temas para as palavras (cidades, cores, times, países, objetos, etc.)
#e níveis de dificuldade (ex: iniciante, intermediário, avançado).

def escolher_palavra(tema):
    if tema == 'frutas':
        return random.choice(['maça', 'pera', 'uva', 'banana', 'abacaxi', 'limão', 'laranja', 'abacate', 'amora'])
    elif tema == 'cidades':
        return random.choice(['rio', 'paris', 'roma', 'nova york', 'tokyo', 'berlim', 'londres', 'pequim', 'moscou'])
    elif tema == 'cores':
        return random.choice(['vermelho', 'azul', 'amarelo', 'verde', 'roxo', 'laranja', 'preto', 'branco', 'rosa'])
    elif tema == 'times':
        return random.choice(['palmeiras', 'vasco', 'joinville', 'flamengo', 'arsenal', 'porto', 'napoli', 'milan'])

def main():
    temas_disponiveis = ['frutas', 'cidades', 'cores', 'times']  
    niveis_dificuldade = ['iniciante', 'intermediário', 'avançado']

    nivel = input("Escolha o nível de dificuldade (iniciante, intermediário, avançado): ").lower()
    while nivel not in niveis_dificuldade:
        print("Nível de dificuldade inválido. Escolha entre iniciante, intermediário ou avançado.")
        nivel = input("Escolha o nível de dificuldade novamente: ").lower()

    tema = input(f"Escolha o tema ({', '.join(temas_disponiveis)}): ").lower()
    while tema not in temas_disponiveis:
        print("Tema inválido. Escolha entre os temas disponíveis.")
        tema = input(f"Escolha o tema novamente ({', '.join(temas_disponiveis)}): ").lower()

    certa = escolher_palavra(tema)
    contador = 5

    for i in range(1, contador + 1):
        print(f"Adivinhe a palavra relacionada ao tema {tema} com {contador - i + 1} tentativas.")
        tent_palavra = input("Informe uma palavra: ")

        if tent_palavra == certa:
            print("Correto! Você acertou.")
            break
        else:
            print(f"Tente novamente, você possui ainda {contador - i} tentativas.")

    if i == contador and tent_palavra != certa:
        print(f"Suas tentativas acabaram. A palavra correta era {certa}")

if __name__ == "__main__":
    main()
