import random, string


def gerar_senha(tamanho):
    if tamanho < 4:
        print("Tamanho muito pequeno! Use pelo menos 5 caracteres para uma senha segura.")
        return None

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = '!@#$%*&¨^ç-=+(),.:?'

    # Garantindo pelo menos um de cada tipo
    senha = [
        random.choice(letras),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Preenchendo o restante da senha com caracteres aleatórios
    todos_os_chars = letras + numeros + simbolos
    senha += [random.choice(todos_os_chars) for _ in range(tamanho - 3)]

    # Embaralhando para não ficar previsível
    random.shuffle(senha)

    return ''.join(senha)

def salvar_senha(senha):
    with open("senhas_geradas.txt", "a") as arquivo:
        arquivo.write(senha + "\n")
    print("Senha salva em 'senhas_geradas.txt'.")

def main():
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        senha = gerar_senha(tamanho)
        if senha:
            print(f"Senha gerada: {senha}")
            salvar_senha(senha)
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()