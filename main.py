import os

from converter import Converter

dir = os.getcwd() + "/input"

def choosingFile(startName : str) -> str :

    files = {}
    for i, file in enumerate(os.listdir(dir), start=1):
        if file.endswith('.csv') and file.startswith(startName):
            files[i] = file
            print(f"{i}. {file}")

    # Demander à l'utilisateur de saisir le numéro du fichier désiré
    num_fichier_cells = int(input("Entrez le numéro du fichier que vous souhaitez sélectionner : "))
    
    # Vérifier si le numéro de fichier est valide
    if num_fichier_cells in files:
        filename = files[num_fichier_cells]
        print("Vous avez sélectionné le fichier :", filename)
        
    else:
        print("Numéro de fichier invalide.")
        exit(1)
    return filename

# Concaténer le chemin du dossier avec le nom du fichier saisi
print("Choix du fichier de cellules")
filenameCells = choosingFile('Export')
pathfilenameCells = os.path.join(dir, filenameCells)

print("Choix du fichier d'identifications")
filenameID = choosingFile('Identifications')
pathfilenameID = os.path.join(dir, filenameID)

#converter = Converter(pathfilename)
#converter.convertToNewFile()
converter = Converter(pathfilenameCells, pathfilenameID)
converter.convertToNewFile()

