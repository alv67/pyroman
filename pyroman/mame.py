import subprocess
import xml.etree.ElementTree as ET


def run_mame_command_and_save_to_file(filename):
    try:
        # Esegue il comando 'mame --listxml' e cattura l'output
        result = subprocess.run(["mame", "-listxml"], capture_output=True, text=True)

        if result.returncode == 0:
            # Il comando è stato eseguito con successo
            xml_data = result.stdout

            # Parsa l'output XML in una struttura ElementTree
            root = ET.fromstring(xml_data)

            # Chiama una funzione per convertire l'albero XML in un dizionario
            # parsed_data = xml_to_dict(root)
            tree = ET.ElementTree(root)
            with open(filename, "wb") as xml_file:
                tree.write(xml_file)

            print(f"Il contenuto è stato salvato nel file '{filename}'.")
        else:
            print("Errore durante l'esecuzione del comando 'mame -listxml'.")
            print("Output di errore:")
            print(result.stderr)
    except FileNotFoundError:
        print("Il comando 'mame' non è presente nel sistema.")


def xml_to_dict(element):
    result = {}

    for child in element:
        # Ricorsivamente converti i figli in dizionari
        child_data = xml_to_dict(child)
        if child.tag in result:
            # Se la chiave esiste già, trasforma il valore in una lista
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_data)
        else:
            result[child.tag] = child_data

    return result


if __name__ == "__main__":
    # Specifica il nome del file XML in cui salvare il contenuto
    xml_filename = "output_mame.xml"

    # Esegui il comando 'mame --listxml' e salva il contenuto in un file XML
    run_mame_command_and_save_to_file(xml_filename)
