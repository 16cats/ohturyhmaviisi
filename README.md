# [TEKA3003 Miniprojekti](https://ohjelmistotuotanto-jyu.github.io/)
![CI](https://github.com/16cats/ohturyhmaviisi/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/gh/16cats/ohturyhmaviisi/branch/main/graph/badge.svg)](https://codecov.io/gh/16cats/ohturyhmaviisi)

Tarkoituksena on tehdä ohjelmisto, jonka avulla voi lisätä latex-tiedostoon lähteitä.

Työn backlogin löydät [täältä](https://jyu.sharepoint.com/:x:/s/OHTUR5/IQDqeg-eeTNzRYoQbwnLpe8MAfN5-x99SziqperxXiQJsB8?e=NHGCvY).

## Käyttöohjeet
Ohjeet komentorivisovelluksen käyttöön.

### Esivaatimukset

#### Python
- On oltava [Python 3.10 tai uudempi versio](https://www.python.org/downloads/).

#### Poetry
- On oltava poetry. Tarkemmat ohjeet käyttöön [täältä](https://ohjelmistotuotanto-jyu.github.io/poetry).

Poetry Windows-asennus:
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Poetry Linux ja macOS-asennus:
```
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
```

Kannattaa olla myös poetry shell asennettuna.
```
poetry self add -poetry-plugin-shell
```

### Varsinainen käyttö (MacOs)
Kloonaa repo:
```
git clone https://github.com/16cats/ohturyhmaviisi.git
```
Mene kloonattuun kansioon:

```
cd ohturyhmäviisi
```
Tee ohjelmasta ajettava:
```
chmod +x run.sh
```
Aja ohjelma: 

```
./run.sh
```

###Varsinainen käyttö (Windows)

Kloonaa repo:
```
git clone https://github.com/16cats/ohturyhmaviisi.git
```
Mene kloonattuun kansioon:

```
cd ohturyhmäviisi
```

Ohjelmakansiossa aja poetry shell:
```
poetry shell
```

Ajetaan varsinainen ohjelma:
```
python -m src.main
```

## DoD

- Toteutetun koodin testikattavuuden tulee olla kohtuullinen
- Asiakas pääsee näkemään kook ajan koodin a testien tilanteen CI-palvelusta
- Koodin ylläpidettävyyden tulee olla mahdollisimman hyvä

* järkevä nimeäminen
* järkevä/selkeä ja perusteltu arkkitehtuuri
* yhtenäinen koodityyli (noudattaa pylintin avulla määriteltyjä sääntöjä).
