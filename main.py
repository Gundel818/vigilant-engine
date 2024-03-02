from converter import Converter

fullfpath = input("Entrez le chemin vers le fichier csv exporté d'EA : ")

converter = Converter(fullfpath)
converter.convertToNewFile()



