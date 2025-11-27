from src.app import App
from src.reference_saver import ReferenceSaver
from src.reference_lister import ReferenceLister

def main():
    app = App()
    saver = ReferenceSaver()
    lister = ReferenceLister()

    viite = None

    while True:
        print("Komennot:")
        print("1 - Lisää viite")
        print("2 - Tallenna viite")
        print("3 - Listaa viitteet")
        print("0 - Lopeta")

        komento = input("> ")

        if komento == "1":
            viite = app.lisaa_viite()
            if viite:
                print("Viite lisätty!")

        elif komento == "0":
            break

        elif komento == "2":
            if viite:
                saver.tallenna(viite)
                print("Viite tallennettu")
                viite = None
            else:
                print("Ei tallennettavaa viitettä!")

        elif komento == "3":
            lister.print_references()

        else:
            print("Huono komento")

if __name__ == "__main__":
    main()
