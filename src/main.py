from .app import App
from .reference_saver import ReferenceSaver
from .reference_lister import ReferenceLister
from .bibtex_exporter import BibtexExporter
from .reference_deleter import ReferenceDeleter
from .reference_tagger import ReferenceTagger



def main():
    app = App()
    saver = ReferenceSaver()
    lister = ReferenceLister()
    exporter = BibtexExporter()
    deleter = ReferenceDeleter()
    tagger = ReferenceTagger()


    viite = None

    while True:
        print("Komennot:")
        print("1 - Lisää viite")
        print("2 - Tallenna viite")
        print("3 - Listaa kaikki viitteet")
        print("4 - Listaa viitteet kirjoittajan mukaan")
        print("5 - Listaa viitteet julkaisuvuoden mukaan")
        print("6 - Listaa viitteet julkaisutyypin mukaan ")
        print("7 - Generoi BibTeX-tiedosto")
        print("8 - Poista viite avaimen perusteella")
        print("9 - Lisää tägi viitteelle")
        print("10 - Muokkaa viitteen tägejä")
        print("11 - Poista viitteen tägit")
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

        elif komento == "7":
            exporter.export()

        elif komento == "8":
            key = input("Anna poistettavan viitteen avain: ")
            if not key:
                print("Et antanut mitään avainta.")
            else:
                poistettu = deleter.delete_by_key(key)
                if poistettu:
                    print(f"Viite [{key}] poistettu.")
                else:
                    print(f"Viitettä [{key}] ei löytynyt.")

        elif komento == "9":
            key = input("Anna viitteen key, johon lisätään tägi: ")
            if not key:
                print("Et antanut mitään avainta.")
            else:
                tag = input("Anna tägin teksti (esim. 'palaa tähän lähteeseen'): ")
                if not tag:
                    print("Et antanut tägiä.")
                else:
                    ok = tagger.add_tag(key, tag)
                    if ok:
                        print(f"Tägi lisätty viitteeseen [{key}].")
                    else:
                        print(f"Viitettä [{key}] ei löytynyt.") 

        elif komento == "10":
            key = input("Anna viitteen avain, jonka tägejä muokataan: ")
            if not key:
                print("Et antanut mitään avainta.")
            else:
                uusi = input("Anna uudet tägit pilkuilla eroteltuna (esim. 'tärkeä, palaa tähän'): ")
                ok = tagger.set_tags(key, uusi)
                if ok:
                    print(f"Viitteen [{key}] tägit päivitetty.")
                else:
                    print(f"Viitettä [{key}] ei löytynyt.")

        elif komento == "11":
            key = input("Anna viitteen avain, jolta poistetaan tägit: ")
            if not key:
                print("Et antanut mitään avainta.")
            else:
                ok = tagger.clear_tags(key)
                if ok:
                    print(f"Viitteen [{key}] tägit poistettu.")
                else:
                    print(f"Viitettä [{key}] ei löytynyt.")
            
        else:
            print("Bad command!")

if __name__ == "__main__":
    main()
