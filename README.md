# vigilant-engine
Convert EA LTE cells export file (CSV format, semicolon delimiter) to NSG Cell File (CSV Format, comma delimiter)

## Choix entre créer un nouveau fichier csv (delimiter ,) et merge avec un fichier déjà existant 

### Option 1 (Nouveau fichier) :
    - Prendre le fichier csv issu de EA
    
    - Dupliquer le fichier (nom arbitraire)
    
    - Choisir quel opérateur garder 
    
    - Supprimer colonnes inutiles

    - Supprimer lignes avec colonnes vides (Colonne NOM)

    - Enlever caractère , dans colonne NOM si besoin
    
    - Renommer et classer les colonnes selon cet ordonnancement : ECellID,CellName,Longitude,Latitude,PCI,EARFCN,Azimuth
    
    - ECellID = eNB * 256 + CID (si 4 CID du même eNB, alors le faire 4 fois)

    - CellName = colonne NOM

    - Azimuth mettre à -1

### Option 2 (Merge avec un fichier NSG déjà existant)

    - Demander à l'utilisateur le fichier EA à convertir

    - Demander à l'utilisateur le fichier NSG existant

    - Dupliquer le fichier NSG (ajouter v2, v3 au nom du fichier par exemple)

    - Exécuter Option 1 tout en regardant à chaque fois, si la ligne n'est pas déjà existante (== comparer colonnes ECellID en particulier (PCI aussi))

    - Demander à l'utilisateur si remplacer ou passer, dans les cas où l'ECellID est pareil mais le PCI est différent
