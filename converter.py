import pandas as pa
from datetime import datetime

class Converter:

    def __init__(self, cellfile : str, idfile : str):
        self.__df = pa.read_csv(cellfile, header=0, sep=';', index_col=False)
        self.__df.set_index('ID', inplace=True)
        self.__id_df = pa.read_csv(idfile, header= 0, sep=';')
        self.__ope = ""


    def removeUselessColumnsandData(self):
        df = self.__df

        df = df.drop(columns=['TAC', 'Date', 'FirstDate', 'LastDate', 'Flag', 'RF'])

        # Supprimer lignes avec colonne 'NOM' vide
        # Garder uniquement lignes sans 'Données insuffisantes' dans colonne 'NOM'
        df = df.dropna(subset=['NOM'])
        df = df[df['NOM'] != 'Données insuffisantes']
        self.__df = df

    def mergingIdinCells(self):
        df = self.__df
        id_df = self.__id_df
        
        df = df.merge(id_df[['eNB', 'Lat']], left_on='eNB', right_on='eNB', how='right')
        df = df.merge(id_df[['eNB', 'Lon']], left_on='eNB', right_on='eNB', how='right')
        df = df.drop(columns=['LAT', 'LON'])

        self.__df = df

    def renameAndReorderColumns(self):
        # Récup les bonnes coordonées depuis le fichier d'identifications pour remplacer sur celui des cellules
        self.mergingIdinCells()
        opeList = ["ORANGE", "BYTEL", "SFR", "FREE"]
        
        df = self.__df

        # Renommage colonnes                                            
        df = df.rename(columns={"eNB": "ECellID", "NOM" : "CellName", "Lat" : "Latitude", "Lon" : "Longitude", "ARFCN" : "EARFCN"})
        df['OP'] = df['OP'].str.upper()

        ope = input("Quel opérateur ? (Orange, ByTel, ..) : ")

        self.setOPE(ope)
        if not self.getOPE() in opeList:
            print("Opérateur non reconnu.")
            exit(1)

        df = df.loc[df['OP'] == self.getOPE()]

        # Calcul ECellID
        df['ECellID'] = (df['ECellID'] * 256) + df['CID']
        df = df.sort_values(by='ECellID')
        
        df.reset_index(drop=True, inplace=True)
        
        # Placement des colonnes dans un certain ordre
        df = pa.DataFrame(df, columns=['ECellID','CellName','Longitude','Latitude', 'PCI', 'EARFCN', 'Azimuth'])
        df['Azimuth'] = -1

        self.__df = df

    def setOPE(self, ope : str):
        ope = ope.upper()
        self.__ope = ope

    def getOPE(self):
        return self.__ope

    def save(self):
        ajd = datetime.now()

        date_actu = ajd.strftime("%Y-%m-%d_%H_%M_%S")
        save = 'NSG_' + self.getOPE() + "_" + date_actu + '.csv'
        self.__df.to_csv('output/' + save, index=False)
        print("Fichier", save, "sauvegardé")

    def convertToNewFile(self):
        self.removeUselessColumnsandData()
        self.renameAndReorderColumns()
        self.save()
        print("Conversion terminée.")
