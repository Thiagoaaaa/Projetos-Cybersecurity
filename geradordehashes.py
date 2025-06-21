import hashlib

# Entrada do usuário
string = input("Digite o texto a ser gerado a hash: ")

# Menu de seleção
menu = int(input('''\n### MENU - ESCOLHA O TIPO DE HASH ###
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o número do hash a ser gerado: '''))

# Processamento
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('\n[+] O hash MD5 da string é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('\n[+] O hash SHA1 da string é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('\n[+] O hash SHA256 da string é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('\n[+] O hash SHA512 da string é: ', resultado.hexdigest())
else:
    print('\n[!] Opção inválida. Por favor, escolha uma opção de 1 a 4.')
