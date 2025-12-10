*** Settings ***
Library    Process

*** Test Cases ***
Käyttäjä voi lisätä viitteen ja listata sen
    # Käynnistä ohjelma
    Start Process    python3    src/main.py    shell=True    alias=app

    # Valitse "1 - Lisää viite"
    Send Process Input    app    1\n

    # Syötä viite
    Send Process Input    app    @book\n
    Send Process Input    app    testkey1\n
    Send Process Input    app    Testikirja\n
    Send Process Input    app    Lauri\n
    Send Process Input    app    2025\n

    # Tallenna viite
    Send Process Input    app    2\n

    # Listaa viitteet (komento 3)
    Send Process Input    app    3\n

    ${output}=    Get Process Output    app

    Should Contain    ${output}    Lauri (2025): Testikirja [testkey1]

    Terminate Process    app