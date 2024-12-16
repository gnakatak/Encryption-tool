tabelaLetra = { 
    'a': ['1', 'r', 0],
    'b': ['2', 's', 0],
    'c': ['3', 't', 0],
    'd': ['4', 'u', 0],
    'e': ['5', 'v', 0],
    'f': ['6', 'w', 0],
    'g': ['7', 'x', 0],
    'h': ['8', 'y', 0],
    'i': ['9', 'z', 0],
    'j': ['a', '!', 0],
    'k': ['b', '@', 0],
    'l': ['c', '#', 0],
    'm': ['d', '$', 0],
    'n': ['e', '%', 0],
    'o': ['f', '^', 0],
    'p': ['g', '&', 0],
    'q': ['h', '*', 0],
    'r': ['i', '(', 0],
    's': ['j', ')', 0],
    't': ['k', '-', 0],
    'u': ['l', '_', 0],
    'v': ['m', '=', 0],
    'w': ['n', '+', 0],
    'x': ['o', '<', 0],
    'y': ['p', '>', 0],
    'z': ['q', '~', 0],
    ' ': [' ', ' ', 0],
}

tabelaNumero = {
    '1': ['a', 't', 'u', '+', 0],
    '2': ['b', 's', 'v', '=', 0],
    '3': ['c', 'r', 'w', '_', 0],
    '4': ['d', 'q', 'x', '-', 0],
    '5': ['e', 'p', 'y', '>', 0],
    '6': ['f', 'o', 'z', '<', 0],
    '7': ['g', 'n', '!', '*', 0],
    '8': ['h', 'm', '@', '&', 0],
    '9': ['i', 'l', '#', '^', 0],
    '0': ['j', 'k', '$', '%', 0],
    ' ': [' ', ' ', ' ', ' ', 0],
    ',': [',', ',', ',', ',', 0],
    '.': ['.', '.', '.', '.', 0]
}

# Decifra números para letras
def number(text):
    resposta = []
    for i in text:
        for j in range(10):
            if i in tabelaNumero[str(j)]:
                resposta.append(j)
    return resposta

def letter1(text):
    resposta = []
    for i in text:
        if i == ' ':  # Preserva espaços
            resposta.append(' ')
        else:
            for j in range(26):
                if i in tabelaLetra[chr(97 + j)]:
                    resposta.append(chr(97 + j))
    return resposta

def letter2(text):
    resposta = []
    for i in text:
        if i == ' ':  # Preserva espaços
            resposta.append(' ')
        else:
            for j in range(26):
                letra = chr(97 + j)
                if i in tabelaLetra[letra][:2]:
                    resposta.append(letra)
    return resposta

# Função principal para decifrar
def decrypter(text, rule):
    if rule == 1:
        return letter1(text)
    elif rule == 2:
        return letter2(text)

# Imprime o texto cifrado
def imprime_cifra(text):
    for i in text:
        print(i, end='')

def zerar():

    for i in tabelaLetra:
        tabelaLetra[i][2] = 0
    for i in tabelaNumero:
        tabelaNumero[i][4] = 0

# Programa principal
if __name__ == "__main__":
    while True:
        print('\nBem-vindo ao programa de cifra!')
        print('Digite 1 para decifrar letras') 
        print('Digite 2 para decifrar números') 
        print('Digite 3 para sair')
        escolha1 = input()

        # Verifique se a entrada foi válida
        if escolha1 == '3':
            print("Saindo do programa...")
            break
        
        elif escolha1 == '1':
            print('\nDigite o tipo de Decifra a ser usada:')
            print('Digite 1 para SIMPLES')
            print('Digite 2 para COMPLEXA')
            escolha2 = input()

            if escolha2 == '1':
                print('Digite o texto a ser decifrado:')
                texto = input()
                resposta = decrypter(texto, 1)
            
            elif escolha2 == '2':
                print('Digite o texto a ser decifrado:')
                texto = input()
                resposta = decrypter(texto, 2)

            imprime_cifra(resposta)
            print()

        elif escolha1 == '2':
            print('Digite o número a ser decifrado:')
            texto = input()
            resposta = number(texto)
            imprime_cifra(resposta)
            print()

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
