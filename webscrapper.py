import requests
from bs4 import BeautifulSoup

url = 'https://ge.globo.com/'

# Fazer a requisição HTTP
response = requests.get(url)

# Verificar se o site respondeu com sucesso
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscando os títulos principais (geralmente dentro de <h2> com classe específica)
    manchetes = soup.find_all('h2')

    print("\n[+] Principais Manchetes do GE.globo.com:\n")
    for i, manchete in enumerate(manchetes):
        texto = manchete.get_text(strip=True)
        if texto:
            print(f"{i+1}. {texto}")
else:
    print("[!] Falha ao acessar o site. Código de status:", response.status_code)
