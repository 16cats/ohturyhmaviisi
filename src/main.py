from .app import App
from .reference_saver import ReferenceSaver
from .reference_lister import ReferenceLister

def main():
    app = App()
    saver = ReferenceSaver()
    lister = ReferenceLister()

    viite = None

    while True:
        print("Komennot:")
        print("1 - Lisää viite")
        print("2 - Tallenna viite")
        print("3 - Listaa kaikki viitteet")
        print("4 - Listaa viitteet kirjoittajan mukaan")
        print("5 - Listaa viitteet julkaisuvuoden mukaan")
        print("6 - Listaa viitteet julkaisutyypin mukaan ")
        print("0 - Lopeta")

        komento = input("> ")

        if komento == "1":
            viite = app.lisaa_viite()
            if viite:
                print("Reference added!")

        elif komento == "0":
            break

        elif komento == "2":
            if viite:
                saver.tallenna(viite)
                print("Reference saved!")
                viite = None
            else:
                print("No references to save!")

        elif komento == "3":
            lister.print_references()

        elif komento == "4":
            nimi = input("Kirjoittajan nimi (tai osa nimeä):")
            lister.print_by_author(nimi)

        elif komento == "5":
            vuosi = input("Julkaisuvuosi: ")
            lister.print_by_year(vuosi)

        elif komento == "6":
            tyyppi = input("Julkaisutyppi (esim @book, @article jne.): ")
            lister.print_by_type(tyyppi)    

        else:
            print("Huono komento!")

        

            

if __name__ == "__main__":
    main()
