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


def main():
    # Create an ArgumentParser object with a description of the program
    parser = argparse.ArgumentParser(description="Useful program to manage and check MAME roms")
    parser.add_argument("--gui", action="store_true", help="Run with GUI")
    parser.add_argument("--config-file", help="Specify a configuration file")
    parser.add_argument("--other-param", help="Other parameters")

    args = parser.parse_args()

    # Check the arguments and take appropriate actions
    if args.gui:
        print("Running with GUI")
        # Call the function to run with GUI
        run_gui()
    elif args.config_file:
        print("Running with the specified configuration file:", args.config_file)
        # Call the function to run with a specific configuration file
        # run_with_config(args.config_file)
    elif args.other_param:
        print("Other parameters:", args.other_param)
    else:
        print("No params are passed!!")
        # Perform other logic based on the passed parameters

if __name__ == "__main__":
    main()
