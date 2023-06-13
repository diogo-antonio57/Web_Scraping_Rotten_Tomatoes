import requests
from bs4 import BeautifulSoup

# Nome do filme
#filme = 'shrek'

def nota_filme(filme):
    # URL da página do filme
    url = f"https://www.rottentomatoes.com/m/{filme}"

    # Fazendo requisição HTTP para a página
    response = requests.get(url)

    # Criando objeto BeautifulSoup a partir do HTML da página
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrando a porcentagem de aprovação do filme na página
    score_section = soup.find('score-board')
    score = score_section['tomatometerscore']
    return score

# Imprimindo a porcentagem de aprovação
#print(score)
