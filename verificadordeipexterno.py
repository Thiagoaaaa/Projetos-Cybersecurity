import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

try:
    print("Consultando o IP externo...")

    resposta = urlopen(url, timeout=10)
    dados = json.load(resposta)

    ip = dados.get('ip', 'Desconhecido')
    org = dados.get('org', 'Desconhecida')
    cidade = dados.get('city', 'Desconhecida')
    pais = dados.get('country', 'Desconhecido')
    regiao = dados.get('region', 'Desconhecida')
    localizacao = dados.get('loc', 'Desconhecida')

    print("\nResultado:")
    print("IP:", ip)
    print("Organização:", org)
    print("Cidade:", cidade)
    print("País:", pais)
    print("Região:", regiao)
    print("Localização (Lat/Lon):", localizacao)

    salvar = input("\nQuer salvar o resultado em um arquivo? (s/n): ")
    if salvar.lower() == 's':
        arquivo = open('ip_detalhes.txt', 'w', encoding='utf-8')
        arquivo.write("IP: " + ip + "\n")
        arquivo.write("Organização: " + org + "\n")
        arquivo.write("Cidade: " + cidade + "\n")
        arquivo.write("País: " + pais + "\n")
        arquivo.write("Região: " + regiao + "\n")
        arquivo.write("Localização (Lat/Lon): " + localizacao + "\n")
        arquivo.close()
        print("Arquivo salvo como ip_detalhes.txt.")

except Exception as erro:
    print("Erro ao consultar o IP:", erro)

