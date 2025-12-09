#!/bin/bash

echo "== Ohturyhmaviisi asennus (macOS) =="

# Tarkista Python
if ! command -v python3 &> /dev/null
then
    echo "Virhe: Python3 ei löytynyt. Asenna Python 3.10+."
    exit 1
fi

# Tarkista Poetry
if ! command -v poetry &> /dev/null
then
    echo "Poetry ei ole asennettuna. Asennetaan..."
    curl -sSL https://install.python-poetry.org | python3 -
    echo "Poetry asennettu!"
    echo "HUOM: Sulje ja avaa terminaali uudestaan tai aja:"
    echo "source \$HOME/.zprofile"
fi

echo ""
echo "== Asennetaan projektin riippuvuudet =="
poetry install --no-root

echo ""
echo "== Aktivoidaan Poetry-ympäristö =="
# Haetaan virtuaaliympäristön polku
VENV_PATH=$(poetry env info --path)

if [ ! -d "$VENV_PATH" ]; then
    echo "Virhe: virtual environment ei löydy!"
    exit 1
fi

# Aktivoidaan ympäristö
source "$VENV_PATH/bin/activate"
echo "Ympäristö aktivoitu: $VENV_PATH"

echo ""
echo "== Käynnistetään sovellus =="
python -m src.main