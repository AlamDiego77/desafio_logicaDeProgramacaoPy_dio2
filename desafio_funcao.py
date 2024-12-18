"""
# 2️⃣ Calculadora de partidas Rankeadas
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

"""

### Criano a função que calcula o rank e o saldo

def calculaRank(vitorias, derrotas):
    
    """Determinando o Rank do Jogador com Base no Numero de vitórias! """

    saldoDeVitorias = vitorias - derrotas

    if vitorias < 10:
        rank = "Ferro"
    elif 11 <= vitorias <= 20:
        rank = "Bronze"
    elif 21 <= vitorias <= 50:
        rank = "Prata"
    elif 51 <= vitorias <= 80:
        rank = "Ouro"
    elif 81 <= vitorias <= 90:
        rank = "Diamante"
    elif 91 <= vitorias <= 100:
        rank = "Lendário"
    else:  # vitorias >= 101
        rank = "Imortal"

    return saldoDeVitorias, rank
  
''' criando a função main que vai solicitar os dados de vitoria e derrota para o user

    vai verificar se o valor é inteiro e valido, se for vai chamar a função calcula rank e passar os paramentros

    Depois vai pegar o retorno da funçao e armazenar nas variaveis de saldo e rank e exibi-los
'''

def main():
    
    while True:
        try:
            vitorias = int(input("Informe a quantidade de vitórias: "))
            derrotas = int(input("Informe a quantidade de derrotas: "))
            break
        except ValueError:
            print("Por favor, insira um numero inteiro valido. ")

    saldo_vitorias, nivel = calculaRank(vitorias, derrotas)


    print(f"O Herói tem saldo de {saldo_vitorias} e está no nível de {nivel}")

if __name__ == "__main__":
    main()