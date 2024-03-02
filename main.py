from converter import Converter
import os

dir = os.getcwd() + "/input"

files = {}
for i, file in enumerate(os.listdir(dir), start=1):
    if file.endswith('.csv'):
        files[i] = file
        print(f"{i}. {file}")

# Demander à l'utilisateur de saisir le numéro du fichier désiré
numero_fichier = int(input("Entrez le numéro du fichier que vous souhaitez sélectionner : "))

# Vérifier si le numéro de fichier est valide
if numero_fichier in files:
    filename = files[numero_fichier]
    print("Vous avez sélectionné le fichier :", filename)
else:
    print("Numéro de fichier invalide.")
    exit(1)

# Concaténer le chemin du dossier avec le nom du fichier saisi
pathfilename = os.path.join(dir, filename)

converter = Converter(pathfilename)
converter.convertToNewFile()



