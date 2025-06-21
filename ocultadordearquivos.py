import ctypes
import os

def ocultar_arquivo(caminho_arquivo):

    atributo_ocultar = 0x02

    # Verificar se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"\n[!] Arquivo '{caminho_arquivo}' não encontrado.")
        return


    retorno = ctypes.windll.kernel32.SetFileAttributesW(caminho_arquivo, atributo_ocultar)

    if retorno:
        print(f"\n[+] Arquivo '{caminho_arquivo}' foi ocultado com sucesso!")
    else:
        print(f"\n[!] Falha ao ocultar o arquivo '{caminho_arquivo}'.")

def main():
    arquivo = input("Digite o nome (ou caminho) do arquivo que deseja ocultar: ")
    ocultar_arquivo(arquivo)

if __name__ == "__main__":
    main()

#Precisa criar um arquivo para ser ocultado (ex: ocultar.txt)