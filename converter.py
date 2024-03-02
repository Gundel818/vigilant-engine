import pandas as pa
import os
from datetime import datetime

class Converter:

    def __init__(self, inputfile : str):
        self.__inputf = inputfile
        self.__df = pa.read_csv(inputfile, header=0, sep=';', index_col=False)
        self.__df.set_index('ID', inplace=True)
        self.__ope = ""



    def removeUselessColumnsandData(self):
        df = self.__df

        # ECellID,CellName,Longitude,Latitude,PCI,EARFCN,Azimuth
        df = df.drop(columns=['TAC', 'Date', 'FirstDate', 'LastDate', 'Flag', 'RF'])

        # Supprimer lignes avec colonne 'NOM' vide
        df = df.dropna(subset=['NOM'])

        # Garder lignes sans 'Données insuffisantes' dans colonne 'NOM
        df = df[df['NOM'] != 'Données insuffisantes']

        self.__df = df

    def renameAndReorderColumns(self):
        df = self.__df
        # Renommage colonnes
        df = df.rename(columns={"eNB": "ECellID", "NOM" : "CellName", "LAT" : "Latitude", "LON" : "Longitude", "ARFCN" : "EARFCN"})

        ope = input("Quel opérateur ? (Orange, Bytel, ..) ")
        self.setOPE(ope)
        df = df.loc[df['OP'] == ope]
        print(df.head())
        
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

        date_actu = ajd.strftime("%Y-%m-%d_%H:%M:%S")
        save = 'NSG_' + self.getOPE() + "_" + date_actu + '.csv'
        self.__df.to_csv('output/' + save, index=False)

    def convertToNewFile(self):
        self.removeUselessColumnsandData()
        self.renameAndReorderColumns()
        self.save()
