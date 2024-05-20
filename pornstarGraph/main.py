from processing import haal_json_bestanddata_op, sla_data_op_in_json, json_naar_csv, haal_ssd_bestanddata_op
from processing import wijzig_json_data, voeg_bestand_toe_aan_json_data, verwerk_los_bestand, lees_sterren
from processing import save_pornstars
from file import Bestand
from tijd import formatteer_uitvoertijd
from zoek import zoekmachine
from selectie import selectiemaker
from geluid import speel_geluid_af
from notatie import noteer_bos, noteer_verwerkingstijd
import time
from variabele import constants


def main() -> None:
    print("\nKies uit de volgende opties:\n")
    print(" - sla de data van de ssd (en hdd) op in het json-bestand (1);")
    print(" - sla de json-data op in het csv-bestand (2);")
    print(" - wijzig de data in het 'hele' json-bestand (3);")
    print(" - wijzig de data van een 'specifieke sleutel' in het json-bestand (4);")
    print(" - voeg een nieuw bestand toe aan het json-bestand (5);")
    print(" - sla nieuwe sterren op / verwijder huidige, dubbele sterren (6);")
    print(" - zoekmachine (7);")
    print(" - maak een willekeurige selectie (8);")
    print(" - noteer bos (9).\n")

    keuze: str = input("Voer hier uw keuze in: ")

    if keuze == '1':
        met_hdd: str = input("\nWilt u ook de hhd-bestanden verwerken (ja/nee): ")
        ook_hdd: bool = False

        if 'j' in met_hdd.lower():
            ook_hdd = True

        starttijd: time = time.time()

        ssd_data: dict[str, dict[str, str | int | float]] = haal_ssd_bestanddata_op(ook_hdd)

        sla_data_op_in_json(ssd_data)
        json_naar_csv()

        eindtijd: time = time.time()
        uitvoertijd: time = eindtijd - starttijd
        uitvoertijd_leesbaar: str = formatteer_uitvoertijd(uitvoertijd)

        speel_geluid_af("geluiden/finish_him.wav", 3)

        print(f"\nHet ophalen van de bestandgegevens van de ssd (en hdd), het opslaan in het json-bestand en het creëren van een csv-bestand van de data heeft {uitvoertijd_leesbaar} geduurd.")

        aantal_bestanden: int = len(ssd_data.keys())
        aantal_datapunten_per_bestand: int = len(ssd_data[constants.SLEUTEL_VOOR_AANTAL_DATAPUNTEN].keys())
        noteer_verwerkingstijd(uitvoertijd_leesbaar, uitvoertijd, aantal_bestanden,
                               aantal_datapunten_per_bestand, ook_hdd)
    elif keuze == '2':
        json_naar_csv()
    elif keuze == '3':
        subsleutel: str = input("\nVoer hier de"
                                " exacte naam van de subsleutel die u wilt aanpassen in (bijv.: \"Bestandtype\"): ")

        print("\nKies nu de operatie uit die u wilt uitvoeren op de data: \n")
        print(" - keuze 1: .upper();")
        print(" - keuze 2: .lower();")
        print(" - keuze 3: .replace().")

        operatie: str = input("\nOperatie: ")

        json_data: dict[str, dict[str, str | int | float]] = haal_json_bestanddata_op()
        gewijzigde_json_data: dict[str, dict[str, str | int | float]] = wijzig_json_data(json_data, subsleutel,
                                                                                         operatie, False)
        sla_data_op_in_json(gewijzigde_json_data)
    elif keuze == '4':
        bestandnaam_sleutel: str = input("\nVoer hier de exacte bestandnaam of een reeks unieke symbolen die erin"
                                         " voorkomen in van het bestand dat uw wilt wijzigen in het json-bestand: ")
        subsleutel: str = input("\nVoer hier de"
                                " exacte naam van de subsleutel die u wilt aanpassen in (bijv.: \"Bestandtype\"): ")

        print("\nKies nu de operatie uit die u wilt uitvoeren op de data: \n")
        print(" - keuze 1: .upper();")
        print(" - keuze 2: .lower();")
        print(" - keuze 3: .replace().")

        operatie: str = input("\nOperatie: ")

        json_data: dict[str, dict[str, str | int | float]] = haal_json_bestanddata_op()
        gewijzigde_json_data: dict[str, dict[str, str | int | float]] = wijzig_json_data(json_data, subsleutel,
                                                                                         operatie, True,
                                                                                         bestandnaam_sleutel)
        sla_data_op_in_json(gewijzigde_json_data)
    elif keuze == '5':
        bestandpad: str = input("\nVoer hier het volledige pad van het bestand in: ").replace("\\", '/').replace('"', '')

        bestand: Bestand = verwerk_los_bestand(bestandpad)
        json_data: dict[str, dict[str, str | int | float]] = haal_json_bestanddata_op()

        voeg_bestand_toe_aan_json_data(json_data, bestand)
    elif keuze == '6':
        sterren_alleen_uniek: set[str] = lees_sterren()

        save_pornstars(sterren_alleen_uniek)
    elif keuze == '7':
        zoekmachine()
    elif keuze == '8':
        grootte_selectie: int = int(input("\nVoer hier de door u gewenste grootte van de selectie in: "))
        selectiemaker(grootte_selectie)
    elif keuze == '9':
        tijd: str = input("\nVoer hier de tijd in (vorm: hh.mm): ")
        volledig_bestandpad: str = input("\nVoer hier het volledig pad van het bosbestand in: ")
        reden: str = input("\nVoer hier de reden in: ")

        noteer_bos(tijd, volledig_bestandpad, reden)
    else:
        print("\nUw keuze is ongeldig; probeer het nogmaals.\n")
        quit()

    print("\nAlle wijzigingen zijn succesvol aangebracht.\n")


if __name__ == "__main__":
    main()
