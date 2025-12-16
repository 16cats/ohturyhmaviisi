# [TEKA3003 Miniprojekti](https://ohjelmistotuotanto-jyu.github.io/)
![CI](https://github.com/16cats/ohturyhmaviisi/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/gh/16cats/ohturyhmaviisi/branch/main/graph/badge.svg)](https://codecov.io/gh/16cats/ohturyhmaviisi)

Tarkoituksena on tehdä ohjelmisto, jonka avulla voi lisätä latex-tiedostoon lähteitä.

Työn backlogin löydät [täältä](https://jyu.sharepoint.com/:x:/s/OHTUR5/IQDqeg-eeTNzRYoQbwnLpe8MAfN5-x99SziqperxXiQJsB8?e=NHGCvY).


## 🌱Esivaatimukset

#### Python & Poetry
- On oltava [Python 3.10 tai uudempi versio](https://www.python.org/downloads/).
- On oltava poetry. Tarkemmat ohjeet käyttöön [täältä](https://ohjelmistotuotanto-jyu.github.io/poetry).

Poetry Windows-asennus:
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Poetry Linux ja macOS-asennus:
```
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
```

Kannattaa olla myös **poetry shell** asennettuna.
```
poetry self add -poetry-plugin-shell
```

## 🌿Varsinainen käyttö (Windows & macOS)

Kloonataan repo ja mennään kansioon:
```
git clone https://github.com/16cats/ohturyhmaviisi.git
cd ohturyhmaviisi
```

Windows:
Suorita komento & ajetaan varsinainen ohjelma
```
Set-ExecutionPolicy -Scope Process RemoteSigned
./run.ps1
```


macOS:
Tee ohjelmasta ajettava & aja ohjelma
```
chmod +x run.sh
./run.sh
```

## 🌳DoD

- Toteutetun koodin testikattavuuden tulee olla kohtuullinen
- Asiakas pääsee näkemään kook ajan koodin a testien tilanteen CI-palvelusta
- Koodin ylläpidettävyyden tulee olla mahdollisimman hyvä:
    * järkevä nimeäminen
    * järkevä/selkeä ja perusteltu arkkitehtuuri
    * yhtenäinen koodityyli (noudattaa pylintin avulla määriteltyjä sääntöjä).

## Miten sovellusta voisi käyttää useamman käyttäjän kesken samassa projektissa? 
Yksi vaihtoehto olisi luoda konsolisovellukselle graafinen käyttöliittymä. Graafisen käyttöliittymän luonti vaatisi paljon tekemistä. Graafisen sovelluksen voisi julkaista web sovelluksena ja silloin sovellukseen tarvittaisiin myös käyttäjätiedot ja sql-tietokantaan mahdollisuudet. Tästä tulisi siis aika paljon tekemistä, mikäli yhteiskehitystä haluaisi siis tehdä verkon välityksellä. 

Yliopiston palvelimella pyörivä sovellus voisi toimia konsolisovelluksena, mutta silloin kaikki olisi kaikille käyttäjille julkista. Eli sovellus periaatteessa toimisi, mutta ei tarkoitetulla tavalla.

Dockerin kautta toimiva yhteiskäyttö olisi myös mahdollista, mutta silloin pitäisi saada myös http endopointit toimimaan käyttäjien kesken. Eli ehkä kaikista toimivin ratkaisu pitkällä aikavälillä olisi luoda sovelluksesta verkkosovellus, jolloin sovellus olisi helpoimmin skaalattavissa kaikille käyttäjille samaan aikaan.
