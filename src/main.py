from src.app import App
from src.reference_saver import ReferenceSaver

def main():
    app = App()
    saver = ReferenceSaver()

    viite = None

    while True:
        print("Komennot:")
        print("1 - Lisää viite")
        print("2 - Tallenna viite")
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

        else:
            print("Huono komento")

if __name__ == "__main__":
    main()
