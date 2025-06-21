import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import re


def start(url):
    wordlist = []

    try:
        source = requests.get(url).text
    except requests.exceptions.RequestException as e:
        print(f"[!] Erro ao acessar a URL: {e}")
        return

    soup = BeautifulSoup(source, 'html.parser')

    # Pegando apenas o texto limpo (removendo scripts e styles)
    for texto in soup.stripped_strings:
        words = re.findall(r'\b\w+\b', texto.lower())  # Quebra por palavras, remove pontuação
        wordlist.extend(words)

   
    word_counts = Counter(wordlist)

    # Exibindo as 10 palavras mais frequentes
    print("\n[+] Top 10 palavras mais frequentes na página:\n")
    for palavra, count in word_counts.most_common(10):
        print(f"{palavra} : {count}")



url_alvo = input("\nDigite a URL para analisar (ex: https://ge.globo.com/): ")
start(url_alvo)
