from src.app import App
from src.reference_saver import ReferenceSaver
from src.reference_lister import ReferenceLister

def main():
    app = App()
    saver = ReferenceSaver()
    lister = ReferenceLister()

    viite = None

    while True:
        print("Commands:")
        print("1 - Add Reference")
        print("2 - Save Reference")
        print("3 - List References")
        print("0 - Exit")

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

        else:
            print("Bad command!")

if __name__ == "__main__":
    main()
