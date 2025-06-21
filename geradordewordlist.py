import itertools

# Função de mutações simples tipo leet
def gerar_variacoes(palavra):
    substituicoes = {
        'a': ['a', '@', '4'],
        'e': ['e', '3'],
        'i': ['i', '1', '!'],
        'o': ['o', '0'],
        's': ['s', '$', '5'],
    }

    lista = ['']
    for letra in palavra:
        novas = []
        if letra.lower() in substituicoes:
            for p in lista:
                for sub in substituicoes[letra.lower()]:
                    novas.append(p + sub)
        else:
            for p in lista:
                novas.append(p + letra)
        lista = novas
    return lista

# Coleta de palavras base
palavras_base = []
print("\nDigite palavras base (ex: nomes, datas, apelidos). Digite 'sair' para terminar.\n")

while True:
    entrada = input("Palavra: ")
    if entrada.lower() == 'sair':
        break
    palavras_base.append(entrada)

# Gera variações + letras maiúsculas
variacoes = set()
for palavra in palavras_base:
    variacoes.update(gerar_variacoes(palavra))
    variacoes.add(palavra.upper())
    variacoes.add(palavra.capitalize())

# Gera combinações de 1 e 2 palavras (para não travar o PC)
combinacoes_finais = set()

print("\nGerando combinações, aguarde...")

for tamanho in range(1, 3):  # Combinar 1 ou 2 palavras
    for combo in itertools.product(variacoes, repeat=tamanho):
        resultado = ''.join(combo)
        if 4 <= len(resultado) <= 12:  # Tamanho de senha
            combinacoes_finais.add(resultado)

# Salva no arquivo
output_file = input("\nNome do arquivo para salvar a wordlist (ex: wordlist.txt): ")

with open(output_file, 'w', encoding='utf-8') as arquivo:
    for item in sorted(combinacoes_finais):
        arquivo.write(item + '\n')

print(f"\n[+] Wordlist salva com sucesso! Total de senhas geradas: {len(combinacoes_finais)}")
print(f"Arquivo: {output_file}")
