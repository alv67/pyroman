import argparse
import os
from pyroman.gui import run_gui


# Funzione per controllare la presenza del file di configurazione
def check_config_file():
    # Controlla se il file pyroman.ini esiste
    if os.path.isfile("pyroman.ini"):
        return True
    else:
        return False


# Funzione per creare un file di configurazione pyroman.ini
def create_default_config():
    # Implementa qui la logica per la creazione del file di configurazione di default
    pass


if __name__ == "__main__":
    # Parsing degli argomenti da linea di comando
    parser = argparse.ArgumentParser(description="Programma con GUI o configurazione")
    parser.add_argument("--gui", action="store_true", help="Esegui con GUI")
    args = parser.parse_args()

    # Controlla se è richiesta la GUI
    if args.gui:
        run_gui()
    else:
        # Controlla la presenza del file di configurazione
        if not check_config_file():
            # Il file di configurazione pyroman.ini non esiste, crea un file di configurazione di default
            create_default_config()
            print("File di configurazione 'pyroman.ini' creato.")
        else:
            print("Il file di configurazione 'pyroman.ini' esiste.")

            # Implementa il resto della logica per l'interazione da console e la configurazione
