import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def consultar_ip_externo():
    url = 'https://ipinfo.io/json'

    try:
        print("\n[+] Consultando informações de IP externo...")

        resposta = urlopen(url, timeout=10)
        dados = json.load(resposta)

        # Extraindo os dados com segurança
        info = {
            "IP": dados.get('ip', 'Não disponível'),
            "Organização (ISP)": dados.get('org', 'Não disponível'),
            "Cidade": dados.get('city', 'Não disponível'),
            "País": dados.get('country', 'Não disponível'),
            "Região": dados.get('region', 'Não disponível'),
            "Localização (Lat/Lon)": dados.get('loc', 'Não disponível')
        }

        return info

    except HTTPError as e:
        print(f"[!] Erro HTTP ao acessar a API: {e.code} - {e.reason}")
    except URLError as e:
        print(f"[!] Erro de conexão: {e.reason}")
    except Exception as e:
        print(f"[!] Erro inesperado: {e}")

    return None

def exibir_resultado(info):
    if info:
        print("\n[+] Detalhes do IP Externo:\n")
        for chave, valor in info.items():
            print(f"{chave}: {valor}")

        # Pergunta se o usuário quer salvar em arquivo
        salvar = input("\nDeseja salvar os resultados em um arquivo .txt? (s/n): ").lower()
        if salvar == 's':
            with open('resultado_ip.txt', 'w', encoding='utf-8') as f:
                for chave, valor in info.items():
                    f.write(f"{chave}: {valor}\n")
            print("\n[+] Resultado salvo como 'resultado_ip.txt'.")

def main():
    info = consultar_ip_externo()
    exibir_resultado(info)

if __name__ == "__main__":
    main()
