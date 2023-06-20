# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Produit le mardi 20 juin 2023

from tkinter import *
import inspect
from typing import Callable

'# lineno() Pour consulter le programme grâce au suivi des prints'
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

root = Tk()
root.geometry("1000x1200")
tab_deux = []  # Liste_itérative[n *= 2] globale.
dic_pairs = {}  # Dictionnaire des nombres pairs avec leurs localisations.
dic_impairs = {}  # Dictionnaire des nombres impairs avec leurs localisations.
dic_terme2, dic_terme3 = {}, {}
# axes_global = {}  # Dictionnaire des dictionnaires


def graphes(tab2, guide, nbr):
    """ Mise en situation matricielle.
    Va influer sur les dimensions du Canvas.
    Dictionnaire-guide.keys(index+type(pair ou pas)), guide.values(Nombre).
    Où, keys = vertical, values = horizontal."""
    long_clefs = (len(guide.keys()) * 13)  # long_clefs = Canvas.height(hauteur visuelle).
    (lineno(), nbr, ' tab2:', tab2[0], '\nguide:', "Len ", len(guide.keys()), 'long_clefs: ', long_clefs)
    # 21 25  graphes.tab2: [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
    #  guide: {(1, 'impair'): 25, (2, 'pair'): 76, (3, 'pair'): 38, ,,, (23, 'pair'): 2, (24, 'impair'): 1}
    # long_clefs:  150
    '''Unification des listes dans un dictionnaire unique.'''
    liste_pair, liste_impair, dico_gen = [], [], {}
    for i in guide.keys():
        if i[1] == 'impair':
            liste_impair.append(guide[i])
            dico_gen[i[0]] = (i, guide[i])
            (lineno(), '_  impair:', guide[i], '\ti:', i)
        else:
            liste_pair.append(guide[i])
            dico_gen[i[0]] = (i, guide[i])
            (lineno(), 'pair:', guide[i], '\ti:', i)
    '# Construction du cadre aux axes.'
    espace_nombres = (len(liste_impair) + len(liste_pair)) + (400 * 2)
    rng_axe = espace_nombres // 2
    interval = espace_nombres // 6
    rng_pai, rng_imp = rng_axe + espace_nombres // 8, rng_axe - espace_nombres // 8
    (lineno(), 'L-impair:', liste_impair, '\nL-pair:', liste_pair, 'Q-espace_nombres:', espace_nombres)
    # 45 L-impair: [25, 19, 29, 11, 17, 13, 5, 1]
    # L-pair: [76, 38, 58, 88, 44, 22, 34, 52, 26, 40, 20, 10, 16, 8, 4, 2] Q-espace_nombres: 744
    "# Ordonner les listes afin d'en tirer les strates horizontales"
    ord_pai, ord_imp = liste_pair.copy(), liste_impair.copy()
    ord_pai.sort()  # En ordre pour avoir le rang horizontal
    ord_imp.sort()  # À retourner, car rangées inversées
    # Voilà ☺
    long_pai, long_imp = len(ord_pai), len(ord_imp)  # Quantité de nombres dans chaque liste.
    (lineno(), 'O-ord_pai:', ord_pai, long_pai, '\nO-ord_imp:', ord_imp, long_imp)
    # 52 O-ord_pai: [2, 4, 8, 10, 16, 20, 22, 26, 34, 38, 40, 44, 52, 58, 76, 88] 16
    # O-ord_imp: [29, 25, 19, 17, 13, 11, 5, 1] 8
    rang_pai = [rng_pai + (x * (interval // long_pai)) for x in range(1, long_pai + 1)]  # Position des nombres
    rang_imp = [rng_imp - (x * (interval // long_imp)) for x in range(1, long_imp + 1)]  # en pixels
    (lineno(), 'rang_pai pairs:', rang_pai, '\nrang_imp impairs: ', rang_imp)
    # 55 Espace pairs: [567, 576, 585, 594, 603, 612, 621, 630, 639, 648, 657, 666, 675, 684, 693, 702]
    # Espace impairs:  [168, 150, 132, 114, 96, 78, 60, 42]
    cant.delete("all")
    cant.config(scrollregion=(0, 0, espace_nombres, long_clefs))
    cant.config(width=espace_nombres, height=long_clefs)
    cant.config(xscrollcommand=hor_bar.set, yscrollcommand=ver_bar.set)
    # r_wid, r_hei = cant.winfo_reqwidth(), cant.winfo_reqheight()
    # print(" r_wid ", r_wid, "  \t r_hei  ", r_hei)

    '# Les trois axes verticaux'
    cant.create_line(rng_imp, 12, rng_imp, long_clefs, width=1, fill='red')
    cant.create_line(rng_axe, 12, rng_axe, long_clefs, width=1, fill='green')
    cant.create_line(rng_pai, 12, rng_pai, long_clefs, width=1, fill='blue')
    '# Correspondance avec la liste croissante des précédents doublés'
    max_lis_all = max(max(liste_pair), max(liste_impair))
    if max_lis_all > tab_deux[-1]:
        pro_deux = tab_deux[-1]
        for i in range(tab_deux[-1], max_lis_all + 2, 2):
            pro_deux *= 2  # pro_deux : Change à chaque fois.
            tab_deux.append(pro_deux)
        (lineno(), 'tab_deux:', tab_deux)

    def terminal(n):
        """Détermine la section paire du nombre n.
            Soit, valeur maxi = 2**sec. Et mini = ((2**sec)//2)+2"""
        sec, org = 0, n
        while n > 1:  # Délimiter la section terminale de n
            n /= 2
            sec += 1
        n_max, n_min = 2**sec, ((2**sec)//2)+2
        prime = [org, sec, n_max, n_min]
        return prime

    "# Phase de finalisation et d'affichage des informations."
    p1xy, p2xy = [], []  # p1xy = Point_départ_arrivée.pair
    i1xy, i2xy = [], []  # Points_départ_arrivée.impair
    dic_terme2.clear()
    dic_terme3.clear()
    dic_pairs.clear()
    dic_impairs.clear()
    for ite in dico_gen.keys():
        type_gen = dico_gen[ite][0][1]  # Partie de la clé où est écrit le type du nombre.
        haut_gen, case_gen = ite, dico_gen[ite][1]  # haut_gen = Vertical, case_gen = Horizontal.
        haut_gen *= 12  # Intervalle vertical entre les nombres.
        ("_*", lineno(), 'haut_gen (vertical):', haut_gen, 'case_gen (horizontal):', case_gen, dico_gen[ite][0])
        (lineno(), '_*  sans-condition type_gen:', type_gen, '\t\tp1xy:', p1xy)
        if type_gen == 'pair':
            unity = dico_gen[ite][1]
            retour = terminal(unity)
            code = retour
            dic_terme2[unity] = code  # Dictionnaires des caractéristiques.
            (" ", lineno(), 'PAIR, unity:', unity, "\t|", retour, "dic_terme2", dic_terme2[unity])
            ind_unity = ord_pai.index(unity)
            case_gen = rang_pai[ind_unity]
            pass_gen = haut_gen, case_gen
            dif_gen = case_gen - rng_pai
            x_corps, y_corps = max(rang_pai) + 24, haut_gen  # Positionne le texte (unity)
            dic_pairs[unity] = []
            (lineno(), 'PAIR, case_gen :', case_gen, '\t unity:', unity, "|", x_corps, y_corps)
            (lineno(), 'pass_gen:', pass_gen, 'rng_pai:', rng_pai, 'dif_gen:', dif_gen)
            if len(p1xy) == 0:
                p1xy.append(pass_gen)
                dic_pairs[unity].append(pass_gen)
                cant.create_text(x_corps, y_corps, text=unity, fill='black')
                cant.create_line(rng_pai, p1xy[0][0], p1xy[0][1], p1xy[0][0], width=1, fill='ivory', dash=(1, 1))
                (lineno(), "Départ pair : <création> (p1xy[1]):", p1xy, ' p2xy :', p2xy)
            else:
                p2xy.append(pass_gen)
                dic_pairs[unity].append(pass_gen)
                (lineno(), 'original pair : (p2xy[1]):', p2xy[0])
                cant.create_line(p1xy[0][1], p1xy[0][0], p2xy[0][1], p2xy[0][0], width=2, fill='blue')
                cant.create_line(rng_pai, p1xy[0][0], p1xy[0][1], p1xy[0][0], width=2, fill='ivory', dash=(1, 1))
                cant.create_text(x_corps, y_corps, text=unity, fill='black')
                '# Première ligne tracée, puis p1xy[départ] devient p2xy[fin précédente)'
                p1xy.clear()  # p1xy = Départ de ligne des nombres pairs.
                p1xy = p2xy.copy()  # p1xy = Copie de l'ancienne fin.
                (lineno(), 'Final pair : (p2xy) :', p2xy, '\n__ Départ pair p1xy :', p1xy)
                p2xy.clear()
            if unity in tab_deux:
                cant.create_text(rng_axe - 12, p1xy[0][0], text=unity, fill='black')
                cant.create_line(rng_axe, p1xy[0][0], rng_pai, p1xy[0][0], width=2, fill='ivory', dash=(1, 1))
        elif type_gen == 'impair':
            unity = dico_gen[ite][1]
            retour = list(terminal(unity))
            code = retour
            dic_terme3[unity] = code  # Dictionnaires des caractéristiques.
            (" ", lineno(), 'IMPAIR, unity:', unity, "\t|", retour, "dic_terme3 code", dic_terme3[unity])
            ind_unity = ord_imp.index(unity)
            case_gen = rang_imp[ind_unity]
            pass_gen = haut_gen, case_gen
            x_corps, y_corps = min(rang_imp) - 24, haut_gen
            dic_impairs[unity] = []
            (" ", lineno(), 'IMPAIR, case_gen:', case_gen, '\t unity:', unity, "|", x_corps, y_corps)
            if len(i1xy) == 0:
                i1xy.append(pass_gen)
                dic_impairs[unity].append(pass_gen)
                cant.create_text(x_corps, y_corps, text=unity, fill='black')
                cant.create_line(rng_imp, i1xy[0][0], i1xy[0][1], i1xy[0][0], width=2, fill='white', dash=(1, 1))
                (lineno(), "\t\t\tDépart impair : <création> (i1xy[1]):", i1xy, 'i2xy :', i2xy)
            else:  # max(rang_imp)
                i2xy.append(pass_gen)
                dic_impairs[unity].append(pass_gen)
                (lineno(), 'original impair : (i2xy[1]):', i2xy)
                cant.create_line(i1xy[0][1], i1xy[0][0], i2xy[0][1], i2xy[0][0], width=2, fill='red')
                cant.create_line(rng_imp, i1xy[0][0], i1xy[0][1], i1xy[0][0], width=2, fill='white', dash=(1, 1))
                cant.create_text(x_corps, y_corps, text=unity, fill='black')
                '# Première ligne tracée, puis p1xy[départ] devient p2xy[fin précédente)'
                i1xy.clear()  # i1xy = Départ de ligne des nombres impairs.
                i1xy = i2xy.copy()  # i1xy = Copie de l'ancienne fin.
                (lineno(), '\t\t\t Final impair : (i2xy[1]):', i2xy, '\n\t\t\t Départ impair i1xy :', i1xy)
                i2xy.clear()
    (lineno(), "dic_pairs", dic_pairs.keys(), "\n dic_impairs", dic_impairs.keys())
    (" ", lineno(), "dic_terme2", dic_terme2.keys(), "\n dic_terme3", dic_terme3.keys())
    for k_imp in dic_impairs.keys():
        k_pai1, k_pai2 = k_imp*3+1, k_imp*2
        (lineno(), "k_imp", k_imp, dic_impairs[k_imp], "\t k_p1", k_pai1, dic_pairs[k_pai1])
        y_deb31, x_deb31 = dic_impairs[k_imp][0]
        y_fin31, x_fin31 = dic_pairs[k_pai1][0]
        cant.create_line(rng_pai, y_fin31, rng_imp, y_deb31, width=2, fill='green', dash=(1, 1),
                         arrow=FIRST, arrowshape=(8, 12, 6))
        if k_pai2 in dic_pairs.keys():  # dic_pairs positions
            y_ava31 = dic_pairs[k_pai2][0]
            cant.create_line(rng_imp, y_deb31, rng_pai, y_ava31[0], width=1, fill='green')
            (lineno(), "k_pai2", k_pai2, dic_pairs[k_pai2])
            # 184 k_pai2 34 [(12, 579)]
        (lineno(), "k_imp", x_deb31, y_deb31, "\t k_pai1", k_pai1, x_fin31, y_fin31)
    '# Dictionnaires des caractéristiques ; *nombre-original, *facteur-exposant, *terminal-maxi, *terminal-mini.'
    """ # Traitement d'affichage des caractéristiques (texte, graphe)
        Texte = Une colonne de trois lignes (*f-e, *t-max, *t-min).
            ¤ Permet d'obtenir la position du nombre transformé parmi la section terminale
                Exemple : .. n = (nombre exemple)
                    a,b=32,18 | c=a/b=1.77 | n(32)/c=18 | n(16)/c=9 """
    for dg in dico_gen.keys():
        """Légende_liste : 
            (*n-o, *f-e, *t-max, *t-min)=*nombre-original, *facteur-exposant, *terminal-maxi, *terminal-mini."""
        nb = dico_gen[dg][1]  # nb = Nombre ordonné à dico_gen
        marge = 120
        (lineno(), "dico_gen dg", dg, dico_gen[dg], "nb", nb, "rang_pai", rang_pai, max(rang_pai))
        if nb in dic_terme2.keys():  # dic_terme2 = Terminal | dic_pairs = Position
            lis_mul, pos_mul = dic_terme2[nb], list(dic_pairs[nb][0])
            taux = str(nb / (lis_mul[2] / lis_mul[3]))
            tex_ = str(lis_mul[1]) + " |" + taux
            if pos_mul[1] == max(rang_pai):
                tex_ += "max"
                marge += 6
            cant.create_text(max(rang_pai)+marge, pos_mul[0], text=tex_, fill='green')
            (lineno(), " dico_gen/lis_mul nb", nb, lis_mul, "pos_mul", pos_mul, "max(rang_pai)", max(rang_pai))
            (lineno(), " dico_gen/dic_terme2 nb", nb, dic_terme2[nb], "\t", dic_pairs[nb])
            # 202  dico_gen/dic_terme2 nb 34 [34, 6, 64, 34] 	 [(12, 579)]
        else:  # dic_terme3 = Terminal | dic_impairs = Position
            lis_mul, pos_mul = dic_terme3[nb], list(dic_impairs[nb][0])
            taux = str(nb / (lis_mul[2] / lis_mul[3]))
            tex_ = str(lis_mul[1]) + " |" + taux
            cant.create_text(min(rang_imp)-marge, pos_mul[0], text=tex_, fill='green')
            (lineno(), " dico_gen/lis_mul nb", nb, lis_mul, "pos_mul", pos_mul, "rang_imp", rang_imp)
            (lineno(), "\n dico_gen/dic_terme3 nb", nb, dic_terme3[nb], "\t", dic_impairs[nb])
            # 209 .../... dico_gen/dic_terme3 nb 13 [13, 4, 16, 10] 	 [(60, 195)]


def traite(nombre):
    """Opération [n/2 ou n*3+1]."""
    '# Série : Cumulative des nombres précédents multipliés par deux [2, 4, 8, 16, 32, 64, 128,,,]'
    pro_deux, nbr_org = 2, nombre
    tab_deux.clear()
    for d in range(2, 33, 2):
        pro_deux *= 2  # pro_deux : Change à chaque fois.
        tab_deux.append(pro_deux)
    stop = True
    dic_partie, long = {}, 1
    while nombre > 1:
        if nombre % 2 == 0:  # Nombre pair entré
            dic_partie[long, 'pair'] = int(nombre)
            long += 1
            nombre /= 2  # On divise le nombre en deux
            (lineno(), 'if traite.nombre:', int(nombre), dic_partie.keys())
        else:  # Nombre impair entré
            dic_partie[long, 'impair'] = int(nombre)
            long += 1
            nombre = nombre * 3 + 1
            (lineno(), "Nombre*3+1 =", nombre, " _________________________Après traitement fonction.traite(n*3+1)")
            # action(nombre)
            (lineno(), '... traite.dic_partie:', dic_partie.keys())
        if nombre in tab_deux:  # tab_deux = Table de la lignée de deux (n/2,n/2,n/2,n/2,,, = 1)
            ind_deux, nombre0 = tab_deux.index(nombre), nombre
            while nombre0 != 1 and stop:
                nombre0 /= 2
                if int(nombre0) == 1:
                    stop = False
    if nombre == 1:
        dic_partie[long, 'impair'] = int(nombre)
    (lineno(), "traite.Dictionnaire élémentaire (pair/impair) dans l'ordre:\n", dic_partie.keys())
    graphes(tab_deux, dic_partie, nbr_org)


def control():
    """Fonction de conversion (str > int)"""
    try:
        nom_bis = int(nombril.get())
        if isinstance(nom_bis, int) and nom_bis > 0:
            (lineno(), 'control.try.nom_bis:', nom_bis, 'type:', type(nom_bis))
            traite(nom_bis)
    except ValueError:
        nombril.insert(0, '2')


'# Entrée utilisateur ☺'
'''#################################################################
#### #      ENTRER      UN      NOMBRE      ENTIER
   #################################################################'''
nombre_max = 0
debut = Frame(root, width=300, height=100, bg='pink')
debut.pack(side='top', ipadx=60, ipady=6)
label = Label(debut, text='Entrez un nombre entier supérieur à 1.')
label.pack()
final = Frame(root, width=600, height=1000,  bg='ivory')
cant = Canvas(final, bg='lightblue')
cant.configure = ('Arial', 8)
hor_bar = Scrollbar(final, orient=HORIZONTAL)
hor_bar.pack(side=BOTTOM, fill=X)
ver_bar = Scrollbar(final, orient=VERTICAL)
ver_bar.pack(side=RIGHT, fill=Y)
hor_bar.config(command=cant.xview)
ver_bar.config(command=cant.yview)
cant.config(xscrollcommand=hor_bar.set, yscrollcommand=ver_bar.set)
final.pack(anchor="center")
cant.pack()
nombril = Entry(debut, justify='center', font='bold')
nombril.pack(padx=6, pady=3, ipadx=60, ipady=6)
nombril.focus()
nombril.bind('<Return>', lambda e: control())

root.mainloop()
