#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Démultiplication(/2) ☺
# Version 3

""" Cette version-3 pour les petits nombres à 7 chiffres,
    sans les afficher les listes."""


def quantum(cas):
    """Selon la quantité de nombres dans la liste terminale."""
    # ('\nQuantum cas: ', cas, ' cap: ', cap)
    for m in cap:  # Initialise en_len.keys() en valeur de liste vide
        en_len[m] = []
        en_fin[m] = []
    for k in cas.keys():  # Range les listes par longueur
        que = len(cas[k])
        en_len[que].append(cas[k][0])
        # ('Q_en_len[que].', en_len[que], que)
    nbr1, nbr2 = 0, 0
    for k in en_len.keys():
        nbr1 += (len(en_len[k]) * k)
        nbr2 = len(en_len[k]) * k
        en_fin[k] = nbr1, nbr2
        # ('Q_en_len : ', k, ' en_len[k] : ', en_len[k], 'nbr1 : ', nbr1, ' nbr2 : ', nbr2)
    ('Q_Pairs.', en_len.keys())


iota = int(input("Nombre à évaluer : "))
glob_part = int(input("0=sans partiels, 1=avec partiels. Votre choix = "))
roma = int(input("0=sans listes, 1=listes, 2=listes>1. Votre choix = "))
# Choisir de voir toutes les listes supérieures à deux nombres.
choix = roma  # Choix 0=nul. 1=Toutes listes. 2=Listes supérieures à un élément.

secteur = 0
origine = iota
while iota > 1:
    iota /= 2
    secteur += 1
section = 2 ** secteur
print('origine :', origine, '. Appartient à la section : ', 2 ** secteur)
if choix:
    if choix == 1:
        print(". Toutes les listes.")
    elif choix == 2:
        print(". Les listes supérieures à une unité.")
en_cas, en_dic, en_len, cap, en_fin = [], {}, {}, [], {}  # Construire listes i%2
pot = eau = True
# Construction du secteur demandé.
for x in range(section, section // 2, -2):
    secte = x
    while not x % 2:
        en_cas.append(x)
        x //= 2
    if en_cas:  # Liste les nombres pairs
        en_dic[secte] = en_cas.copy()
    if choix == 0 and eau:
        eau = False
        print(". Le choix zéro n'est pas affichable.")
    elif choix == 1:
        if pot:
            pot = False
            print('Dico = ', en_dic[section], '  \t\t Terminale = ', len(en_dic[section]))
        else:
            print('Dico = ', en_dic[secte], '    \t\t\t Longueur = ', len(en_dic[secte]))
    elif choix == 2:
        if len(en_dic[secte]) > 1:
            print('Dico = ', en_dic[secte], '    \t\t\t Longueur = ', len(en_dic[secte]))
    x_cap = len(en_dic[secte])
    if x_cap not in cap:
        cap.append(x_cap)
    en_cas.clear()
cap.sort()
quantum(en_dic)

print('\n Résultats Globaux')
print('Origine = ', origine, '. Appartient à la section : ', 2 ** secteur)
long_max = len(en_dic[max(en_dic.keys())])  # Où l'exposant de la mantisse 2
print('Longueur terminale = ', long_max, " = L'exposant de 2")
nbr_list = max(en_dic.keys()) // 4  # Nombre total des listes
print('Nombre    listes = ', nbr_list, ' = Le nombre total des listes')
par_list = (nbr_list - 1) // 3  # Nombre de parties trilog
print('Partie    listes = ', par_list,
      ' = Le nombre de parties trilog. Il reste = ', (nbr_list - 1) - (par_list * 3))
sec_list = long_max - 2  # Longueur de la plus grande sous-liste
print('Section   listes = ', sec_list, ' = La longueur de la plus grande sous-liste')
print('Cap = ', cap, ' = Liste les longueurs des listes ')
# ☺
if glob_part:
    print('\n Résultats Partiels')  # en_le et en_fin = Précisions quantitatives
    debut, grade, viel = ' _ ', '♦', '☺'
    for c in cap:  # c = Une quantité dans la liste cap
        c_cap = en_len[c][:8]  # Liste les listes de même longueur
        soluce = c * len(c_cap)  # 
        nbr_liste = int(en_fin[c][1]) // c  # Même quantité d'éléments des listes
        print('c=', c, "c_cap=", c_cap, '\n\tQuantités (cumulées, partielles)', en_fin[c], '\tNbr_liste//c= ',
              nbr_liste)

# Définition de la mesure de la section terminale
""" Une section terminale = Une des organisations régulières des nombres pairs.   _[Voir # Visite des terminales]_***
La section  terminale = De max(liste) à max(liste)/2+2 
    = [2=min(liste), max(liste)=2**n], séquence les listes fondamentales précédentes.***
En faisant ; maxi = max(liste fondamentale) = 64 || Alors ; max(liste fondamentale)/2+2 = 34...........
= Longueur de la liste terminale 64 = 64/4 = La section 64 a 16 nombres pairs index.    _[Voir # Liste mesurable]_
    Les 16 index sont des listes desquelles ou non-divisibles par 2 aux quotients pairs.
    Liste = Un nombre calculé à n%4 (le reste du quotient du diviseur 4 sur n) = 0.
        [Débat n%4=2] = (n/4=impair) = Liste avec un seul élément.
        [Débat n%4=0] L'index est divisé par deux tant que [n%2!=0], puis il est ajouté à la liste."""

# Visite des sections terminales
""" 
*** Terminal  4 [4, 2] 	 ____ ____ Terminal = 4 		len(vec): 2
*** Terminal  8 [8, 4, 2] 	 ____ ____ Terminal = 8 		len(vec): 3
*** Terminal  16 [16, 8, 4, 2] 	 ____ ____ Terminal = 16 		len(vec): 4
*** Terminal  32 [32, 16, 8, 4] 	 ____ ____ Terminal = 32 		len(vec): 5
*** Terminal  64 [64, 32, 16, 8] 	 ____ ____ Terminal = 64 		len(vec): 6
*** Terminal  128 [128, 64, 32, 16] 	 ____ ____ Terminal = 128 		len(vec): 7
*** Terminal  256 [256, 128, 64, 32] 	 ____ ____ Terminal = 256 		len(vec): 8
*** Terminal  512 [512, 256, 128, 64] 	 ____ ____ Terminal = 512 		len(vec): 9
*** Terminal  1024 [1024, 512, 256, 128] 	 ____ ____ Terminal = 1024 		len(vec): 10
*** Terminal  2048 [2048, 1024, 512, 256] 	 ____ ____ Terminal = 2048 		len(vec): 11
*** Terminal  4096 [4096, 2048, 1024, 512] 	 ____ ____ Terminal = 4096 		len(vec): 12
*** Terminal  8192 [8192, 4096, 2048, 1024] 	 ____ ____ Terminal = 8192 		len(vec): 13
*** Terminal  16384 [16384, 8192, 4096, 2048] 	 ____ ____ Terminal = 16384 		len(vec): 14
*** Terminal  32768 [32768, 16384, 8192, 4096] 	 ____ ____ Terminal = 32768 		len(vec): 15
*** Terminal  65536 [65536, 32768, 16384, 8192] 	 ____ ____ Terminal = 65536 		len(vec): 16
*** Terminal  131072 [131072, 65536, 32768, 16384] 	 ____ ____ Terminal = 131072 		len(vec): 17
*** Terminal  262144 [262144, 131072, 65536, 32768] 	 ____ ____ Terminal = 262144 		len(vec): 18
"""

# Comment mesurer la section terminale
""" À une section terminale correspond une suite régulière de nombres pairs indexés.
***          La section  terminale = De max(liste fondamentale) à max(liste fondamentale)/2+2                  .***
***          La liste à  indexions = De max(liste[0]) à min(liste[-1] divisible par deux)                      .***
Premier temps non terminé ici mais dans la version 4 ☺
"""

# Liste minimale 2(1*2)
"""
Nombre à évaluer : 2
0=sans partiels, 1=avec partiels. Votre choix = 1
0=sans listes, 1=avec listes, 2=listes>1µ. Votre choix = 1
origine : 2 . Appartient à la section :  2
Dico =  [2]   			 Longueur Terminale =  1

 Résultats Globaux
Origine =  2 . Appartient à la section :  2
Longueur terminale =  1  = L'exposant de 2
Nombre    listes =  0  = Le nombre total des listes
Partie    listes =  -1  = Le nombre de parties trilog. Il reste =  2
Section   listes =  -1  = La longueur de la plus grande sous-liste
Cap =  [1]  = Liste les longueurs des listes 

 Résultats Partiels
Ci:  1 [2] Quantités (cumulées, partielles) (1, 1) 
*	Nbr liste//c=  1
"""

# Liste trilog 3(2*2)
"""
Nombre à évaluer : 3
0=sans partiels, 1=avec partiels. Votre choix = 0
0=sans listes, 1=avec listes, 2=listes>1µ. Votre choix = 1
origine : 3 . Appartient à la section :  4
. Toutes les listes.
Dico =  [4, 2]   		 Terminale =  2

 Résultats Globaux
Origine =  3 . Appartient à la section :  4
Longueur terminale =  2  = L'exposant de 2
Nombre    listes =  1  = Le nombre total des listes
Partie    listes =  0  = Le nombre de parties trilog. Il reste =  0
Section   listes =  0  = La longueur de la plus grande sous-liste
Cap =  [2]  = Liste les longueurs des listes 
"""
# Liste 16(8*2)
"""
Nombre à évaluer : 16
0=sans partiels, 1=avec partiels. Votre choix = 0
0=sans listes, 1=listes, 2=listes>1. Votre choix = 1
origine : 16 . Appartient à la section :  16
. Toutes les listes.
Dico =  [16, 8, 4, 2]   		 Terminale =  4
Dico =  [14]     			 Longueur =  1
Dico =  [12, 6]     			 Longueur =  2
Dico =  [10]     			 Longueur =  1

 Résultats Globaux
Origine =  16 . Appartient à la section :  16
Longueur terminale =  4  = L'exposant de 2
Nombre    listes =  4  = Le nombre total des listes
Partie    listes =  1  = Le nombre de parties trilog. Il reste =  0
Section   listes =  2  = La longueur de la plus grande sous-liste
Cap =  [1, 2, 4]  = Liste les longueurs des listes 
"""
# Liste 32(16*2)
"""
Nombre à évaluer : 31
0=sans partiels, 1=avec partiels. Votre choix = 0
0=sans listes, 1=avec listes, 2=listes>1µ. Votre choix = 1
origine : 31 . Appartient à la section :  32
. Toutes les listes.
Dico =  [32, 16, 8, 4, 2]   		 Terminale =  5
Dico =  [30]     			 Longueur =  1
Dico =  [28, 14]     			 Longueur =  2
Dico =  [26]     			 Longueur =  1
Dico =  [24, 12, 6]     			 Longueur =  3
Dico =  [22]     			 Longueur =  1
Dico =  [20, 10]     			 Longueur =  2
Dico =  [18]     			 Longueur =  1

 Résultats Globaux
Origine =  31 . Appartient à la section :  32
Longueur terminale =  5  = L'exposant de 2
Nombre    listes =  8  = Le nombre total des listes
Partie    listes =  2  = Le nombre de parties trilog. Il reste =  1
Section   listes =  3  = La longueur de la plus grande sous-liste
Cap =  [1, 2, 3, 5]  = Liste les longueurs des listes
"""

# Liste 64(32*2)
""" 
Nombre à évaluer : 64
0=sans listes, 1=avec listes, 2=listes>1. Votre choix = 1
origine : 64 . Appartient à la section :  64
Dico =  [64, 32, 16, 8, 4, 2]   			 Longueur Terminale =  6
Dico =  [62]     			 Longueur =  1
Dico =  [60, 30]     			 Longueur =  2
Dico =  [58]     			 Longueur =  1
Dico =  [56, 28, 14]     			 Longueur =  3
Dico =  [54]     			 Longueur =  1
Dico =  [52, 26]     			 Longueur =  2
Dico =  [50]     			 Longueur =  1
Dico =  [48, 24, 12, 6]     			 Longueur =  4
Dico =  [46]     			 Longueur =  1
Dico =  [44, 22]     			 Longueur =  2
Dico =  [42]     			 Longueur =  1
Dico =  [40, 20, 10]     			 Longueur =  3
Dico =  [38]     			 Longueur =  1
Dico =  [36, 18]     			 Longueur =  2
Dico =  [34]     			 Longueur =  1

 Résultats Globaux
Origine =  64 . Appartient à la section :  64
Longueur terminale =  6  = La l'exposant de 2
Nombre    listes =  16  = Le nombre total des listes
Partie    listes =  5  = Le nombre de parties trilog. Il reste =  0
Section   listes =  4  = La longueur de la plus grande sous-liste

 Résultats Partiels
Ci:  1 [62, 58, 54, 50, 46, 42, 38, 34] Quantités (cumul, partiel) (8, 8) 
*	Nbr liste//c=  8
Ci:  2 [60, 52, 44, 36] Quantités (cumul, partiel) (16, 8) 
*	Nbr liste//c=  4
Ci:  3 [56, 40] Quantités (cumul, partiel) (22, 6) 
*	Nbr liste//c=  2
Ci:  4 [48] Quantités (cumul, partiel) (26, 4) 
*	Nbr liste//c=  1
Ci:  6 [64] Quantités (cumul, partiel) (32, 6) 
*	Nbr liste//c=  1
"""
# Liste 128(64*2)
"""_______________________________________________________________________________
Nombre à évaluer : 99
0=sans partiels, 1=avec partiels. Votre choix = 0
0=sans listes, 1=avec listes, 2=listes>1µ. Votre choix = 1
origine : 99 . Appartient à la section :  128
. Toutes les listes.
Dico =  [128, 64, 32, 16, 8, 4, 2]   		 Terminale =  7
Dico =  [126]     			 Longueur =  1
Dico =  [124, 62]     			 Longueur =  2
Dico =  [122]     			 Longueur =  1
Dico =  [120, 60, 30]     			 Longueur =  3
Dico =  [118]     			 Longueur =  1
Dico =  [116, 58]     			 Longueur =  2
Dico =  [114]     			 Longueur =  1
Dico =  [112, 56, 28, 14]     			 Longueur =  4
Dico =  [110]     			 Longueur =  1
Dico =  [108, 54]     			 Longueur =  2
Dico =  [106]     			 Longueur =  1
Dico =  [104, 52, 26]     			 Longueur =  3
Dico =  [102]     			 Longueur =  1
Dico =  [100, 50]     			 Longueur =  2
Dico =  [98]     			 Longueur =  1
Dico =  [96, 48, 24, 12, 6]     			 Longueur =  5
Dico =  [94]     			 Longueur =  1
Dico =  [92, 46]     			 Longueur =  2
Dico =  [90]     			 Longueur =  1
Dico =  [88, 44, 22]     			 Longueur =  3
Dico =  [86]     			 Longueur =  1
Dico =  [84, 42]     			 Longueur =  2
Dico =  [82]     			 Longueur =  1
Dico =  [80, 40, 20, 10]     			 Longueur =  4
Dico =  [78]     			 Longueur =  1
Dico =  [76, 38]     			 Longueur =  2
Dico =  [74]     			 Longueur =  1
Dico =  [72, 36, 18]     			 Longueur =  3
Dico =  [70]     			 Longueur =  1
Dico =  [68, 34]     			 Longueur =  2
Dico =  [66]     			 Longueur =  1

 Résultats Globaux
Origine =  99 . Appartient à la section :  128
Longueur terminale =  7  = L'exposant de 2
Nombre    listes =  32  = Le nombre total des listes
Partie    listes =  10  = Le nombre de parties trilog. Il reste =  1
Section   listes =  5  = La longueur de la plus grande sous-liste
Cap =  [1, 2, 3, 4, 5, 7]  = Liste les longueurs des listes 
"""
# Liste section terminale 256 (128*2)
"""Nombre à évaluer : 180
0=sans partiels, 1=avec partiels. Votre choix = 0
0=sans listes, 1=avec listes, 2=listes>1µ. Votre choix = 2
origine : 180 . Appartient à la section :  256
. Les listes supérieures à une unité.
Dico =  [256, 128, 64, 32, 16, 8, 4, 2]     			 Longueur =  8
Dico =  [252, 126]     			 Longueur =  2
Dico =  [248, 124, 62]     			 Longueur =  3
Dico =  [244, 122]     			 Longueur =  2
Dico =  [240, 120, 60, 30]     			 Longueur =  4
Dico =  [236, 118]     			 Longueur =  2
Dico =  [232, 116, 58]     			 Longueur =  3
Dico =  [228, 114]     			 Longueur =  2
Dico =  [224, 112, 56, 28, 14]     			 Longueur =  5
Dico =  [220, 110]     			 Longueur =  2
Dico =  [216, 108, 54]     			 Longueur =  3
Dico =  [212, 106]     			 Longueur =  2
Dico =  [208, 104, 52, 26]     			 Longueur =  4
Dico =  [204, 102]     			 Longueur =  2
Dico =  [200, 100, 50]     			 Longueur =  3
Dico =  [196, 98]     			 Longueur =  2
Dico =  [192, 96, 48, 24, 12, 6]     			 Longueur =  6
Dico =  [188, 94]     			 Longueur =  2
Dico =  [184, 92, 46]     			 Longueur =  3
Dico =  [180, 90]     			 Longueur =  2
Dico =  [176, 88, 44, 22]     			 Longueur =  4
Dico =  [172, 86]     			 Longueur =  2
Dico =  [168, 84, 42]     			 Longueur =  3
Dico =  [164, 82]     			 Longueur =  2
Dico =  [160, 80, 40, 20, 10]     			 Longueur =  5
Dico =  [156, 78]     			 Longueur =  2
Dico =  [152, 76, 38]     			 Longueur =  3
Dico =  [148, 74]     			 Longueur =  2
Dico =  [144, 72, 36, 18]     			 Longueur =  4
Dico =  [140, 70]     			 Longueur =  2
Dico =  [136, 68, 34]     			 Longueur =  3
Dico =  [132, 66]     			 Longueur =  2

 Résultats Globaux
Origine =  180 . Appartient à la section :  256
Longueur terminale =  8  = L'exposant de 2
Nombre    listes =  64  = Le nombre total des listes
Partie    listes =  21  = Le nombre de parties trilog. Il reste =  0
Section   listes =  6  = La longueur de la plus grande sous-liste
Cap =  [1, 2, 3, 4, 5, 6, 8]  = Liste les longueurs des listes """

# Liste section terminale 512 (256*2)
"""Nombre à évaluer : 500
0=sans partiels, 1=avec partiels. Votre choix = 0
0=sans listes, 1=listes, 2=listes>1. Votre choix = 2
origine : 500 . Appartient à la section :  512
. Les listes supérieures à une unité.
Dico =  [512, 256, 128, 64, 32, 16, 8, 4, 2]   		 Terminale =  9
Dico =  [510]     			 Longueur =  1
Dico =  [508, 254]     			 Longueur =  2
Dico =  [506]     			 Longueur =  1
Dico =  [504, 252, 126]     			 Longueur =  3
Dico =  [502]     			 Longueur =  1
Dico =  [500, 250]     			 Longueur =  2
Dico =  [498]     			 Longueur =  1
Dico =  [496, 248, 124, 62]     			 Longueur =  4
Dico =  [494]     			 Longueur =  1
Dico =  [492, 246]     			 Longueur =  2
Dico =  [490]     			 Longueur =  1
Dico =  [488, 244, 122]     			 Longueur =  3
Dico =  [486]     			 Longueur =  1
Dico =  [484, 242]     			 Longueur =  2
Dico =  [482]     			 Longueur =  1
Dico =  [480, 240, 120, 60, 30]     			 Longueur =  5
Dico =  [478]     			 Longueur =  1
Dico =  [476, 238]     			 Longueur =  2
Dico =  [474]     			 Longueur =  1
Dico =  [472, 236, 118]     			 Longueur =  3
Dico =  [470]     			 Longueur =  1
Dico =  [468, 234]     			 Longueur =  2
Dico =  [466]     			 Longueur =  1
Dico =  [464, 232, 116, 58]     			 Longueur =  4
Dico =  [462]     			 Longueur =  1
Dico =  [460, 230]     			 Longueur =  2
Dico =  [458]     			 Longueur =  1
Dico =  [456, 228, 114]     			 Longueur =  3
Dico =  [454]     			 Longueur =  1
Dico =  [452, 226]     			 Longueur =  2
Dico =  [450]     			 Longueur =  1
Dico =  [448, 224, 112, 56, 28, 14]     			 Longueur =  6
Dico =  [446]     			 Longueur =  1
Dico =  [444, 222]     			 Longueur =  2
Dico =  [442]     			 Longueur =  1
Dico =  [440, 220, 110]     			 Longueur =  3
Dico =  [438]     			 Longueur =  1
Dico =  [436, 218]     			 Longueur =  2
Dico =  [434]     			 Longueur =  1
Dico =  [432, 216, 108, 54]     			 Longueur =  4
Dico =  [430]     			 Longueur =  1
Dico =  [428, 214]     			 Longueur =  2
Dico =  [426]     			 Longueur =  1
Dico =  [424, 212, 106]     			 Longueur =  3
Dico =  [422]     			 Longueur =  1
Dico =  [420, 210]     			 Longueur =  2
Dico =  [418]     			 Longueur =  1
Dico =  [416, 208, 104, 52, 26]     			 Longueur =  5
Dico =  [414]     			 Longueur =  1
Dico =  [412, 206]     			 Longueur =  2
Dico =  [410]     			 Longueur =  1
Dico =  [408, 204, 102]     			 Longueur =  3
Dico =  [406]     			 Longueur =  1
Dico =  [404, 202]     			 Longueur =  2
Dico =  [402]     			 Longueur =  1
Dico =  [400, 200, 100, 50]     			 Longueur =  4
Dico =  [398]     			 Longueur =  1
Dico =  [396, 198]     			 Longueur =  2
Dico =  [394]     			 Longueur =  1
Dico =  [392, 196, 98]     			 Longueur =  3
Dico =  [390]     			 Longueur =  1
Dico =  [388, 194]     			 Longueur =  2
Dico =  [386]     			 Longueur =  1
Dico =  [384, 192, 96, 48, 24, 12, 6]     			 Longueur =  7
Dico =  [382]     			 Longueur =  1
Dico =  [380, 190]     			 Longueur =  2
Dico =  [378]     			 Longueur =  1
Dico =  [376, 188, 94]     			 Longueur =  3
Dico =  [374]     			 Longueur =  1
Dico =  [372, 186]     			 Longueur =  2
Dico =  [370]     			 Longueur =  1
Dico =  [368, 184, 92, 46]     			 Longueur =  4
Dico =  [366]     			 Longueur =  1
Dico =  [364, 182]     			 Longueur =  2
Dico =  [362]     			 Longueur =  1
Dico =  [360, 180, 90]     			 Longueur =  3
Dico =  [358]     			 Longueur =  1
Dico =  [356, 178]     			 Longueur =  2
Dico =  [354]     			 Longueur =  1
Dico =  [352, 176, 88, 44, 22]     			 Longueur =  5
Dico =  [350]     			 Longueur =  1
Dico =  [348, 174]     			 Longueur =  2
Dico =  [346]     			 Longueur =  1
Dico =  [344, 172, 86]     			 Longueur =  3
Dico =  [342]     			 Longueur =  1
Dico =  [340, 170]     			 Longueur =  2
Dico =  [338]     			 Longueur =  1
Dico =  [336, 168, 84, 42]     			 Longueur =  4
Dico =  [334]     			 Longueur =  1
Dico =  [332, 166]     			 Longueur =  2
Dico =  [330]     			 Longueur =  1
Dico =  [328, 164, 82]     			 Longueur =  3
Dico =  [326]     			 Longueur =  1
Dico =  [324, 162]     			 Longueur =  2
Dico =  [322]     			 Longueur =  1
Dico =  [320, 160, 80, 40, 20, 10]     			 Longueur =  6
Dico =  [318]     			 Longueur =  1
Dico =  [316, 158]     			 Longueur =  2
Dico =  [314]     			 Longueur =  1
Dico =  [312, 156, 78]     			 Longueur =  3
Dico =  [310]     			 Longueur =  1
Dico =  [308, 154]     			 Longueur =  2
Dico =  [306]     			 Longueur =  1
Dico =  [304, 152, 76, 38]     			 Longueur =  4
Dico =  [302]     			 Longueur =  1
Dico =  [300, 150]     			 Longueur =  2
Dico =  [298]     			 Longueur =  1
Dico =  [296, 148, 74]     			 Longueur =  3
Dico =  [294]     			 Longueur =  1
Dico =  [292, 146]     			 Longueur =  2
Dico =  [290]     			 Longueur =  1
Dico =  [288, 144, 72, 36, 18]     			 Longueur =  5
Dico =  [286]     			 Longueur =  1
Dico =  [284, 142]     			 Longueur =  2
Dico =  [282]     			 Longueur =  1
Dico =  [280, 140, 70]     			 Longueur =  3
Dico =  [278]     			 Longueur =  1
Dico =  [276, 138]     			 Longueur =  2
Dico =  [274]     			 Longueur =  1
Dico =  [272, 136, 68, 34]     			 Longueur =  4
Dico =  [270]     			 Longueur =  1
Dico =  [268, 134]     			 Longueur =  2
Dico =  [266]     			 Longueur =  1
Dico =  [264, 132, 66]     			 Longueur =  3
Dico =  [262]     			 Longueur =  1
Dico =  [260, 130]     			 Longueur =  2
Dico =  [258]     			 Longueur =  1

 Résultats Globaux
Origine =  500 . Appartient à la section :  512
Longueur terminale =  9  = L'exposant de 2
Nombre    listes =  128  = Le nombre total des listes
Partie    listes =  42  = Le nombre de parties trilog. Il reste =  1
Section   listes =  7  = La longueur de la plus grande sous-liste
Cap =  [1, 2, 3, 4, 5, 6, 7, 9]  = Liste les longueurs des listes
"""

# Pied
