# ohturyhmaviisi
https://ohjelmistotuotanto-jyu.github.io/

Tarkoituksena on tehdä ohjelmisto, jonka avulla voi lisätä latex tiedostoon lähteitä.

Työn backlogin löydät täältä:
https://jyu.sharepoint.com/:x:/s/OHTUR5/IQDqeg-eeTNzRYoQbwnLpe8MAfN5-x99SziqperxXiQJsB8?e=NHGCvY

# Käyttöohjeet
## Esivaatimukset

### Python
- On oltava Python 3.10 tai uudempi versio (https://www.python.org/downloads/).

### Poetry
- On oltava poetry. Tarkemmat ohjeet löytyvät täältä: https://ohjelmistotuotanto-jyu.github.io/poetry

Windows-asennus:
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

Linux ja macOS-asennus:
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -

Kannattaa olla myös shell asennettuna.
poetry self add -poetry-plugin-shell

## Varsinainen käyttö
Kloonaa repo:
git clone https://github.com/16cats/ohturyhmaviisi.git

Aja poetry shell:
poetry shell

Ajetaan varsinainen ohjelma:
python -m src.main
