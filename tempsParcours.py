#!/usr/bin/env python
from datetime import datetime
import requests
LocFile='RsFile.csv' # Fichier dans lequel sont enregistés les résultats
fo=open(LocFile,"a")
key='LaClé'  # remplacer par une clé d'API donnée par Google
def get_tp(porg,pdst,key):
    su="https://maps.googleapis.com/maps/api/distancematrix/json?"
    sp= "origins="+porg+"&destinations="+pdst+"&departure_time=now&"    
    url = su+sp+"key="+key
    r = requests.get(url)
    datJ = r.json()
    dtr=datJ["rows"][0]['elements'][0]['duration_in_traffic']['value']
    return dtr

# La matrice suivante permet d'interroger sur plusieurs OD
# 1ere colonne : nom de l'OD, 2eme colonne : coordonnées origine, 3eme colonne : coordonnées  destination
ODmat=[	["A7_L2_D4","43.337693,5.376957","43.348418,5.370695"],
     ["A7_D4_Ayg","43.348418,5.370695","43.360103,5.362025"],
     ["A7_Ayg_StAn","43.360103,5.362025","43.373955,5.360963"],
     ["A7c_StA_L2","43.378427,5.354983","43.347444,5.371587"],
     ["ConvStA","43.401886,5.346848","43.378427,5.354983"],
     ["FinA7","43.320583,5.377639","43.306009,5.375182" ]
     ];
Nod=len(ODmat)
#Horodatage de la requête
timest = datetime.utcnow().strftime('%Y-%m-%dT%H:%M')
file ='fl'+'.csv'
RsStr=''
for i in range(Nod):
    tt=get_tp(ODmat[i][1],ODmat[i][2],key)
    RsStr=ODmat[i][0]+','+str(tt)+','+timest 
    ws=RsStr+'\n'
    fo.write(ws)      
fo.close()


