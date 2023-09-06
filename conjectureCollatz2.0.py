#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Conjecture-Collatz2.0
# Produit le mardi 20 juin 2023

from tkinter import *
import math
import inspect
from typing import Callable

'# lineno() Pour consulter le programme grâce au suivi des prints'
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

root = Tk()
root.geometry("1600x1600")
tab_deux = []  # Liste_itérative[n *= 2] globale.
dic_pairs = {}  # Dictionnaire des nombres pairs pour leurs localisations.
dic_impairs = {}  # Dictionnaire des nombres impairs pours leurs localisations.
dic_terme2, dic_terme3 = {}, {}  # Dictionnaires (pair/impair) sections terminales


def graphes(tab2, guide, nbr):
    """ Mise en situation matricielle.
    Va influer sur les dimensions du Canvas.
    Dictionnaire-guide, keys (index+type (pair ou pas)), guide.values (Nombre).
    Où, keys = vertical, values = horizontal."""
    long_clefs = (len(guide.keys()) * 13)  # long_clefs = Canvas.height(haut_lg visuelle).
    long_guide = (len(guide.keys()) * 12)  # long_guide = Profondeur des axes
    (lineno(), nbr, ' tab2:', tab2, '\nguide:', "Len ", len(guide.keys()), 'long_clefs: ', long_clefs)
    # 21 25  graphes.tab2: [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
    #  guide: {(1, 'impair'): 25, (2, 'pair'): 76, (3, 'pair'): 38, ,,, (23, 'pair'): 2, (24, 'impair'): 1}
    # long_clefs:  150
    '''Unification des listes dans un dictionnaire unique.'''
    liste_pair, liste_impair, dico_gen = [], [], {}
    for i in guide.keys():
        if i[1] == 'impair':
            liste_impair.append(guide[i])
            dico_gen[i[0]] = (i, guide[i])
            (lineno(), '_  liste_impair:', guide[i], '\ti:', i)
        else:
            liste_pair.append(guide[i])
            dico_gen[i[0]] = (i, guide[i])
            (lineno(), '_  liste_pair:', guide[i], '\ti:', i)
    '# Construction du cadre aux axes.'
    espace_nombres = (len(liste_impair) + len(liste_pair)) + (600 * 2)
    rng_axe = espace_nombres // 2
    interval = espace_nombres // 6
    rng_pai, rng_imp = rng_axe + espace_nombres // 8, rng_axe - espace_nombres // 8
    (lineno(), 'L-impair:', liste_impair, '\nL-pair:', liste_pair, 'Q-espace_nombres:', espace_nombres)
    # 45 L-impair : [25, 19, 29, 11, 17, 13, 5, 1]
    # L-pair : [76, 38, 58, 88, 44, 22, 34, 52, 26, 40, 20, 10, 16, 8, 4, 2] Q-espace_nombres : 744
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
    cant.bind_all("<MouseWheel>", lambda n: molette(n))

    def molette(event):
        cant.yview_scroll(int(-1 * (event.delta / 120)), "units")

    '# Les trois axes verticaux'
    cant.create_line(rng_imp, 12, rng_imp, long_guide, width=1, fill='red')
    cant.create_line(rng_axe, 12, rng_axe, long_guide, width=1, fill='green')
    cant.create_line(rng_pai, 12, rng_pai, long_guide, width=1, fill='blue')
    (lineno(), "long_guide", long_guide)
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
        n_max, n_min = 2 ** sec, ((2 ** sec) // 2) + 2
        prime = [org, sec, n_max, n_min]
        return prime

    "# Phase de finalisation et d'affichage des informations."
    liste_gen = []
    for ite in dico_gen.keys():
        ote = dico_gen[ite][1]
        liste_gen.append(ote)
    (lineno(), "liste_gen", liste_gen)
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
                cant.create_line(p1xy[0][1], p1xy[0][0], p2xy[0][1], p2xy[0][0], width=3, fill='blue',
                                 joinstyle=ROUND, capstyle=ROUND)
                cant.create_line(rng_pai, p1xy[0][0], p1xy[0][1], p1xy[0][0], width=2, fill='ivory', dash=(1, 1))
                cant.create_text(x_corps, y_corps, text=unity, fill='black')
                '# Première ligne tracée, puis p1xy[départ] devient p2xy[fin précédente)'
                p1xy.clear()  # p1xy = Départ de ligne des nombres pairs.
                p1xy = p2xy.copy()  # p1xy = Copie de l'ancienne fin.
                (lineno(), 'Final pair : (p2xy) :', p2xy, '\n__ Départ pair p1xy :', p1xy)
                p2xy.clear()
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
                cant.create_line(i1xy[0][1], i1xy[0][0], i2xy[0][1], i2xy[0][0], width=3, fill='red',
                                 joinstyle=ROUND, capstyle=ROUND)
                cant.create_line(rng_imp, i1xy[0][0], i1xy[0][1], i1xy[0][0], width=2, fill='white', dash=(1, 1))
                cant.create_text(x_corps, y_corps, text=unity, fill='black')
                '# Première ligne tracée, puis p1xy[départ] devient p2xy[fin précédente)'
                i1xy.clear()  # i1xy = Départ de ligne des nombres impairs.
                i1xy = i2xy.copy()  # i1xy = Copie de l'ancienne fin.
                (lineno(), '\t\t\t Final impair : (i2xy[1]):', i2xy, '\n\t\t\t Départ impair i1xy :', i1xy)
                i2xy.clear()
    (lineno(), "dic_pairs", dic_pairs, "\n dic_impairs", dic_impairs, "*LocalisationS*")
    (" ", lineno(), "dic_terme2", dic_terme2.keys(), "\n dic_terme3", dic_terme3.keys())
    #
    '# Dictionnaires des caractéristiques ; *nombre-original, *facteur-exposant, *terminal-maxi, *terminal-mini.'
    """ # Traitement d'affichage des caractéristiques (texte, graphe)
        Texte = Une colonne de trois lignes (*f-e, *t-max, *t-min).
            ¤ Permet d'obtenir la position du nombre transformé parmi la section terminale
                Exemple : .. n = (nombre exemple)
                    a,b=32,18 | c=a/b=1.77 | n(32)/c=18 | n(16)/c=9 """
    tip, tab_tip, lis_tip, dic_taux = 0, {}, [], {}
    tip_pai, tip_imp = [], []
    ob = -1
    """Légende_liste :
     dic_terme2.3 = (*n-o, *f-e, *t-max, *t-min)=*nombre-original, *facteur-exposant, *terminal-maxi, *terminal-mini.
     tab_tip = Espace de représentation graphique combinant les clefs communes."""
    for dg in dico_gen.keys():
        nb = dico_gen[dg][1]  # nb = Nombre ordonné à dico_gen
        tab_tip[nb] = []  # Séries des nombres%2 (False/True)
        marge = 120
        (lineno(), "*** dico_gen DG", dico_gen[dg], "DG", dg, "NB", nb)
        if nb in dic_terme2.keys():  # dic_terme2 = Terminal | dic_pairs = Position
            '''
            Pour t=[34, 6, 64, 34], t[0] = Point d'orgue,
            t[1]= Exposant de la mantisse deux _ t.max[2]= 2**Exposant _ t.min[3]= (t[2]/2)+2
                ♦ Max/min.exemple : 64(max)/34(min) =  1.8823529411764706
                ♦ Max/min = Intervalle régulier relatif à la section exposée.
            Quel taux pour les autres nombres pairs de la section(64>n>34) ?
                a,b,c,d = [34, 6, 64, 34]
                    ♦ (c-a)/(c-d) = Résultat multiplié par cent = Pourcentage dans une section.
                    ♦ (c-a)/(c-(c/2)) = Résultat multiplié par cent = Pourcentage entre deux sections.
            '''
            lis_mul, pos_mul = dic_terme2[nb], list(dic_pairs[nb][0])
            taxi = 100 * ((lis_mul[0] - (lis_mul[2] / 2)) / (lis_mul[2] - (lis_mul[2] / 2)))
            taux = "{:.2f}".format(taxi)
            dic_taux[nb] = taux, dic_terme2[nb][1]
            (lineno(), "\ndic_taux:", dic_taux, "\n")
            tex_ = str(lis_mul[1]) + " | " + taux + " %"
            (lineno(), "texte :", tex_, "dic_terme2[nb]:", dic_terme2[nb])
            if pos_mul[1] == max(rang_pai):
                tex_ += " max"
                marge += 6
            tip += 1  # Compte le nombre de divisions par deux successives
            if tip > 1:
                tab_tip[ob].append(nb)  # Séries des nombres%2 (False=0), mémoriser commun(n/2=Entier)
                tab_tip.pop(nb, None)  # Efface les clefs vides communes
                (lineno(), " *tip>1* NB", nb, "OB", ob, "\t tip", tip, tab_tip[ob])
            else:
                tip_pai.append(nb)
                ob = nb  # Copie la clef majeure (if nb in dic_terme2.keys())
                tab_tip[nb].append(nb)  # Séries des nombres%2 (False=0), garder la clef majeure.
                lis_tip.append(nb)  # Liste des clefs utilisées
                cant.create_text(max(rang_pai) + marge, pos_mul[0], text=tex_, fill='green')
                (lineno(), " *top* NB", nb, "OB", ob, "\t tip", tip, tab_tip[nb])
            (lineno(), " lis_mul nb", nb, lis_mul, "pos_mul", "pos_mul", "max(rang_pai)", "max(rang_pai), lis_tip")
            (lineno(), "d_terme2 NB", nb, dic_terme2[nb], "\t .", dic_pairs[nb], "OB", ob, "\t tip", tab_tip[ob])
            #
        else:  # dic_terme3 = Terminal | dic_impairs = Position
            tip_imp.append(nb)
            tip = 0  # Remise à zéro du nombre de divisions par deux successives
            tab_tip[nb].append(nb)  # Séries des nombres%2 (True>0), impair non divisé par deux.
            lis_tip.append(nb)  # Liste des clefs utilisées
            lis_mul, pos_mul = dic_terme3[nb], list(dic_impairs[nb][0])
            taxi = 100 * ((lis_mul[0] - (lis_mul[2] / 2)) / (lis_mul[2] - (lis_mul[2] / 2)))
            taux = "{:.2f}".format(taxi)
            if nb != 1:
                dic_taux[nb] = taux, dic_terme3[nb][1]
            (lineno(), "\ndic_taux:", dic_taux, "\n")
            tex_ = str(lis_mul[1]) + " | " + taux + " %"
            cant.create_text(min(rang_imp) - marge, pos_mul[0], text=tex_, fill='green')
            (lineno(), " dico_gen/lis_mul nb", nb, lis_mul, "pos_mul", "pos_mul", "rang_imp", "rang_imp")
            (lineno(), " dico_gen/dic_terme3 nb", nb, dic_terme3[nb], "\t", dic_impairs[nb])
            # 209 .../... dico_gen/dic_terme3 nb 13 [13, 4, 16, 10] 	 [(60, 195)]
    (lineno(), "\ndic_taux:", dic_taux, "\n")
    #
    ''' # Affichage de tab_tip
    # dic_terme2, dic_terme3 = Dictionnaires (pairs/impairs) sections terminales |[52, 6, 64, 34]|
    # dic_pairs, dic_impairs = Dictionnaires (pairs/impairs) avec leurs localisations |[(36, 638)]|
    # tab_tip = Dictionnaire (pairs/impairs) démultiplications des quotients (n/2) |tip [52, 26]|'''
    (lineno(), "max(rang_pai)", max(rang_pai), "max(rang_imp)", max(rang_imp))
    (lineno(), "tip_pai", tip_pai, "tip_imp", tip_imp)
    (lineno(), "final.winfo ", final.winfo_width(), final.winfo_height())
    (lineno(), "cant.winfo ", cant.winfo_width(), cant.winfo_height())
    "# Arrangement des taux des implications en pourcentage, à partir de l'axe central."
    bord_p1, bord_p2, bord_i1, bord_i2 = rng_axe + 1, rng_pai - 1, rng_imp + 1, rng_axe  # Axe pair et axe impair
    (lineno(), "Bordures impaires ", bord_i1, bord_i2, " paires ", bord_p1, bord_p2)
    for kp in tab_tip.keys():
        (lineno(), kp, tab_tip[kp])
        if not kp % 2:  # Capter les termes, les localisations des quotients incluses
            (lineno())
            '# Les localisations'
            loc_y = dic_pairs[kp][0][0]
            haut_lg = len(tab_tip[kp]) * 11  # L'y pour l'épaisseur de la ligne
            haut_kp = loc_y + 6 + (len(tab_tip[kp]) * 6)  # L'y pour la haut_lg de la ligne
            # bord_p1, bord_p2 = Définition des longueurs des lignes paires
            lis_mul, pos_mul = dic_terme2[kp], list(dic_pairs[kp][0])
            taxi = 100 * ((lis_mul[0] - (lis_mul[2] / 2)) / (lis_mul[2] - (lis_mul[2] / 2)))
            esp_kp = ((bord_p2 - bord_p1) * taxi) / 100
            cant.create_line(bord_p1, haut_kp, bord_p2, haut_kp, width=haut_lg, fill='lightsteelblue')
            cant.create_line(bord_p1, haut_kp, bord_p1 + esp_kp, haut_kp, width=haut_lg // 2, fill='lavender')
            (lineno(), "d_trm2", dic_terme2[kp], "\t\td_pai", dic_pairs[kp], "\t\tpair tip", tab_tip[kp])
            # 276 d_trm2 [34, 6, 64, 34] 		d_pai [(12, 612)] 		pair tip [34]
            (lineno(), "haut_lg, KP", kp, "bord_p1", bord_p1, "bord_p2", bord_p2)
            # 278 haut_lg, KP 34 bord_p1 410 bord_p2 505
        else:
            ind_loc = tip_imp.index(kp)
            (lineno(), "ind_loc", ind_loc, tip_imp[ind_loc])
            if tip_imp[ind_loc] != 1:
                loc_y2 = dic_impairs[tip_imp[ind_loc]][0][0]  # Localisation verticale (y) nombre en cours
                loc_y3 = dic_impairs[tip_imp[ind_loc + 1]][0][0]  # Localisation verticale (y) nombre suivant
                (lineno(), "loc_y2", loc_y2, "loc_y3", loc_y3)
                (lineno(), "*\tloc_y3-loc_y2=", loc_y3 - loc_y2, "\t*\t(loc_y3-loc_y2)/12=", (loc_y3 - loc_y2) / 12)
                haut_lg = ((loc_y3 - loc_y2) / 12) * 6  # L'y pour l'épaisseur de la ligne
                haut_kp = loc_y2 + ((loc_y3 - loc_y2) / 2)  # L'y pour la haut_lg de la ligne
                (lineno(), "H haut_kp", haut_kp, "haut_lg", haut_lg)
                # bord_i1, bord_i2 = Définition des longueurs des lignes impaires
                lis_mul, pos_mul = dic_terme3[kp], list(dic_impairs[kp][0])
                taxi = 100 * ((lis_mul[0] - (lis_mul[2] / 2)) / (lis_mul[2] - (lis_mul[2] / 2)))
                esp_kp = ((bord_i2 - bord_i1) * taxi) / 100
                cant.create_line(bord_i1, haut_kp, bord_i2, haut_kp, width=haut_lg, fill='pink')  # haut_lg
                cant.create_line(bord_i2, haut_kp, bord_i2 - esp_kp, haut_kp, width=haut_lg // 2, fill='mistyrose')
            (lineno(), "  d_trm3", dic_terme3[kp], "\t\td_imp", dic_impairs[kp], "\t\timpair tip", tab_tip[kp])
            # 297 d_trm3 [17, 5, 32, 18] 		d_imp [(24, 174)] 		impair tip [17]
            (lineno(), "KP", kp, "bord_i1", bord_i1, "bord_i2", bord_i2)
            # 299 KP 17 bord_i1 309 bord_i2 404
    #
    # Tracer les pointillés connectés (n/2) (n3+1)
    '''Flèches pointillées d'un départ nombre1 vers arrivée fléchée à nombre2.'''
    for k_imp in dic_impairs.keys():
        k_pai1, k_pai2 = k_imp * 3 + 1, k_imp * 2
        (lineno(), "k_imp", k_imp, dic_impairs[k_imp], "\t k_p1", k_pai1, dic_pairs[k_pai1])
        y_deb31, x_deb31 = dic_impairs[k_imp][0]
        y_fin31, x_fin31 = dic_pairs[k_pai1][0]
        cant.create_line(rng_pai, y_fin31, rng_imp, y_deb31, width=3, fill='red', dash=(1, 1),
                         arrow=FIRST, arrowshape=(8, 12, 6))
        if k_pai2 in dic_pairs.keys():  # dic_pairs positions
            y_ava31 = dic_pairs[k_pai2][0]
            cant.create_line(rng_pai, y_ava31[0], rng_imp, y_deb31, width=3, fill='blue', dash=(1, 1),
                             arrow=LAST, arrowshape=(8, 12, 6))
            (lineno(), "k_pai2", k_pai2, dic_pairs[k_pai2])
            # 184 k_pai2 34 [(12, 579)]
        (lineno(), "k_imp", x_deb31, y_deb31, "\t k_pai1", k_pai1, x_fin31, y_fin31)
    # Révisions...
    (lineno(), "  dic_terme2", dic_terme2.keys(), "  dic_terme3", dic_terme3.keys(), " Mantisse. Exposant. Section.")
    (lineno(), "tip_pai", tip_pai, "tip_imp", tip_imp)
    (lineno(), "  liste_pair", liste_pair, "\n  liste_impair", liste_impair, " Mantisse. Exposant. Section.")
    (lineno(), "°°° Écriture des paramètres choisis pour leurs utilités °°°")
    #
    # Écriture des paramètres choisis pour leurs utilités
    ''' On commence par le nombre qui est à l'origine des traitements [entre (n/2) et (3*n+1)].
        1- nombre_origine = ?
        2- nombre_listes = len(liste_pair) + len(liste_impair)  # listes_(pair impair)
        3- mantisse, exposant, section = 2, ?, ?  # section = mantisse exposée par l'exposant.
        4- nombre_trilogies = Production du ou des premières sous-section(s)
        4.a-    Définition : À une section correspond une quantité de nombres communs,
                les sections sont réparties suivant les axes des milieux en dégradation
                des milieux, des nombres et des quantités d'éléments listés.
        ?- parcours_ligne = ?  # Le relief horizontal suivant la séquence des sections.
        ?- zone_basse = ?  # Les listes des informations verticalement listées.
            5.a     Les pourcentages selon les sections
    '''
    """(lineno(), "Étape 1- nombre_origine = nbr", nbr, "liste_gen", liste_gen)
    ''' # Mantisse, exposant, section : Dans dic_terme2 et dic_terme3. Accessible via liste_générique_nbr's
        # dic_terme2[34] = [34, 6, 64, 34] et, dic_terme3[17] = [17, 5, 32, 18]'''
    (lineno(), "Étape 2- nombre_listes = len(liste_pair) + len(liste_impair)")
    (lineno(), "Étape 3- mantisse, exposant, section = 2, ?, ?")  # dic_terme2.3[unity]
    (lineno(), "| Étape 4- trilogie, sous-section = nombre_listes / 3, liste les quantités... \n",
          "|\tLa période fondamentale : Concerne la section initiale. \n",
          "|\tLes périodes globales : Concerne tous les nombres, sections, en mode graphique.\n",
          "|\t\tAccompagnées de : Lignes_nombres, lignes_sections, sur une surface définie.", lineno())
    ("Étape 4- ", lineno())
    ("Étape 4- ", lineno())
    (lineno(), "Étape ?- parcours_ligne = ?")
    (lineno(), "Étape ?- zone_basse = ?\n")"""
    # Pour délimiter les coordonnées d'écriture des paramètres
    '''Liste_pair_impair[Listes nombres produits]'''
    min_gau = (dic_impairs[max(liste_impair)][0][1]) - 10  # Marge gauche = -120
    max_dro = (dic_pairs[max(liste_pair)][0][1]) + 10  # Marge droite = +120
    lig_hau = (dic_impairs[1][0][0]) + 15
    neo_len = long_clefs + 600
    print(lineno(), "\t\t\tParamètres Fenêtre long_clefs", long_clefs, "neo_len", neo_len)
    #
    "# Réglage des polices"
    f_titre = ("Times", 11)  # Police des rubriques
    f_ruban = ("Courier", 10)  # Police des descriptions
    c_ovale = ("Times", 14)  # Police des rubriques
    (lineno(), "^^^^^^^^ f_titre", f_titre, "\t |", f_ruban)

    # RECTANGLE SERVICE ******************* DÉBUT STATISTIQUES ************************ RECTANGLE SERVICE
    cant.config(scrollregion=(0, 0, espace_nombres, neo_len))
    cant.config(width=espace_nombres, height=neo_len)
    cant.config(xscrollcommand=hor_bar.set, yscrollcommand=ver_bar.set)
    cant.create_rectangle(min_gau - 130, lig_hau + 6, max_dro + 130, neo_len, fill="lavender", width=0)
    cant.create_rectangle(min_gau, lig_hau, max_dro, neo_len, fill="thistle", width=0)
    cant.create_rectangle(min_gau - 120, lig_hau + 18, min_gau + 12, lig_hau + 32, fill='linen', width=0)

    #
    "# Écriture des quantités de nombres (Qµ_pairs. Qµ_impairs. Qµ_total)"
    h_txt, v_txt = min_gau - 66, lig_hau + 24
    pose = h_txt  # Mémorisation : Position coordonnée horizontale (de gauche à droite)
    t_lis = "Totalité des nombres"  # Libellé
    h_txt += 12  # Position coordonnée horizontale du Libellé
    h_lib = h_txt  # Position coordonnée horizontale du Libellé
    print(lineno(), "POSE horizontale", "Libellé \t\th_lib : ", h_lib, "|POSE verticale ***********v_txt:", v_txt)
    cant.create_text(h_txt, v_txt, text=t_lis, fill='black', font=f_titre)
    t_tot1, t_tot2 = len(liste_pair), len(liste_impair)  # Totalité des longueurs des listes (pair/impair)
    t_tot = str(t_tot1 + t_tot2)  # Totalité des longueurs des listes (pair/impair)
    (lineno(), "______ t_tot:", t_tot, "\t t_tot1.2:", t_tot1, t_tot2)
    h_txt += 102  # Position coordonnée horizontale du total (pairs + impairs)
    h_tot = h_txt  # Position coordonnée horizontale du total (pairs + impairs)
    print(lineno(), "POSE horizontale", "Total \t\t\th_tot : ", h_tot, "|POSE verticale ***********v_txt:", v_txt)
    t_lib = "Section originale"
    cant.create_rectangle(min_gau - 120, v_txt + 18, min_gau + 12, v_txt + 32, fill='linen', width=0)
    cant.create_text(h_lib, v_txt + 24, text=t_lib, fill='black', font=f_titre)
    cant.create_text(h_txt, v_txt, text=t_tot, fill='black', font=f_titre, justify="center")
    loc_aux, loc_bas = "Qµ.pairs : ", "Qµ.impairs : "  # Définitions des rubriques
    qua_tic = (((max_dro + 120) - h_txt) // 2) + h_txt  # Position horizontale du grand texte centré
    h_big = qua_tic
    print(lineno(), "POSE horizontale", "Grand-texte  \th_big :\t", h_big, "|POSE verticale ***********v_txt:", v_txt)
    big_txt = loc_aux + str(t_tot1) + '  _(&)_  ' + loc_bas + str(t_tot2)
    cant.create_text(qua_tic, v_txt, text=big_txt, fill='navy', font=f_ruban, justify="center")
    (lineno(), "*** pose:", pose, type(pose), "\t h_txt:", h_txt, "v_txt:", v_txt, "\n")

    #
    "# Écriture de la section du nombre original (Origine. Mantisse. Exposant. Section)"
    dic_2, dic_3 = list(dic_terme2.keys()), list(dic_terme3.keys())
    (lineno(), "_*_* dic_2:", dic_2, "dic_3:", dic_3)
    if nbr == dic_2[0]:  # nbr = Le premier nombre saisi par l'utilisateur.
        num = dic_terme2[nbr]  # Dictionnaire contenant (num, exposant, section, section[mini])
    else:
        num = dic_terme3[nbr]
    (lineno(), "_ else _ pose:", pose, "\t num:", num, "\tdic_terme",)
    or1, or2, or3 = "Nombre original : ", "Exposant : ", "Section : "
    man, exp, io0, mix = 2, num[1], num[2], num[3]  # dic_terme2.3[unity]
    cal_txt = or1 + str(num[0]) + "\t" + or2 + str(exp) + "\t" + or3 + str(io0)
    v_txt += 24  # Position verticale par ligne ajoutée
    (lineno(), "Ligne verticale ***********v_txt:", v_txt)
    (lineno(), "*** \t h_txt:", h_txt, "v_txt:", v_txt, "\tqua_tic", qua_tic, "\n")
    (lineno(), "pose:", pose, "\n dic_terme2.3:", dic_terme2, "\n", dic_terme3)
    cant.create_text(qua_tic, v_txt, text=cal_txt, fill='navy', font=f_ruban, justify="center")

    #
    """# Écriture du reste trilogique information
        de,     période fondamentale"""
    v_txt += 18  # Position verticale par ligne ajoutée
    cant.create_rectangle(min_gau - 120, v_txt, min_gau + 12, v_txt + 14, fill='linen', width=0)
    (lineno(), "Ligne verticale ***********v_txt:", v_txt)
    ("\n☺", lineno(), "\nen,     périodes fondamentales (voir lignes n°343 à 346)")
    #  Traitement du cas original faisant référence au nombre initial saisit par l'utilisateur.
    # Choix utilisateur original et la partie décorative de la trilogie fondamentale.
    t3_lib = "Section paire"  # Choix utilisateur original.
    h3_tot = (io0 - mix) // 2  #
    h4_tot, h5_tot = h3_tot // 3, h3_tot % 3
    n3_tot = str(h3_tot)
    s3, s_tab = exp, [exp]
    while s3 > 1:
        if s3 == exp:
            s3 -= 2
        else:
            s3 -= 1
        s_tab.append(s3)  # s_tab = Liste les exposants rencontrés.
    h3_big = "Nombre de trilogies : " + str(h4_tot) + "\t\t Reste = " + str(h5_tot) + "\n" + str(s_tab)
    "Conditionné au taux de caractères par ligne (Format écran-utilisateur)."
    if len(str(s_tab)) > (max_dro - min_gau):
        print(lineno(), " * s_tab:", s_tab, " * ")
    cant.create_text(h_lib, v_txt + 6, text=t3_lib, fill='black', font=f_titre)
    cant.create_text(h_tot, v_txt + 6, text=n3_tot, fill='black', font=f_titre, justify="center")
    cant.create_text(h_big, v_txt + 14, text=h3_big, fill='navy', font=f_ruban, justify="center")
    (lineno(), "n3_tot", n3_tot, "s_tab", s_tab, "len(str())", len(str(s_tab)))
    # Fin du choix utilisateur original, et début des périodes globales.

    """# Écriture du reste trilogique information
    en,     périodes globales (voir lignes n°343 à 346)"""
    # Pour l'ensemble des périodes le dictionnaire dic_taux renseigne : Nombres. Pourcentages. Exposants.
    # Pour les sections entières[tip_pai/tip_imp] ou communes[liste_pair/liste_impair] des nombres :
    ("\n☺", lineno(), "\nen,     périodes globales (voir lignes n°343 à 346)")
    print(lineno(), "Les sections communes", "\tliste_pair", liste_pair, "\n  liste_impair", liste_impair)
    print(lineno(), "Les sections entières", "\ttip_pai", tip_pai, "tip_imp", tip_imp)
    ("\n", lineno(), """ Emplacement du graphisme.
    La façade est circulaire, elle est composée de cercles, un cercle égale une section (entière ou commune).
    Priorité aux sections entières ayant un périmètre élargi, afin d'y superposer les sections communes.
    Les éléments des sections sont soumis au modulo(%6), et rayonner parmi les cercles.""")
    v_txt += 52
    # Les sections ordonnées
    lis_sec = []
    for val in dic_taux.values():
        va1, va2 = val
        if va2 not in lis_sec:
            lis_sec.append(va2)
    print(lineno(), "lis_sec :", lis_sec)
    # 469 lis_sec : [6, 5, 4, 3, 2, 1]
    # Le cadrage des graphismes
    o_color, color6 = "grey", ["navy", "yellow", "blue", "red", "violet", "orange"]
    axe_x, axe_y = ((max_dro - min_gau) // 2) + min_gau - 360, (((neo_len - 14) - v_txt) // 2) + v_txt
    centre0 = axe_x, axe_y  # Les coordonnées du point central des sections
    centre1 = axe_x + 210, axe_y  # Les coordonnées du point central des sections
    cant.create_rectangle(min_gau, v_txt, max_dro, neo_len - 14, width=1, outline="grey")
    cant.create_line(h_lib, v_txt, h_big, v_txt, width=30, fill='pink', capstyle=ROUND)
    label0 = "Les graphismes : Les cercles (base%6) et les barres (2D)"
    cant.create_text(h_tot + (h_tot // 2), v_txt, text=label0, fill='black', font=f_titre)
    cant.create_oval(centre0[0] - 210, centre0[1] - 210, centre0[0] + 210, centre0[1] + 210, width=0, fill=o_color)
    cant.create_line(centre1[0] - 210, centre1[1], max_dro, centre1[1], width=432, fill=o_color, capstyle=ROUND)
    # cant.create_oval(centre1[0] - 210, centre1[1] - 210, centre1[0] + 210, centre1[1] + 210, width=1, fill="ivory")
    print("************CERCLES********SECTIONS*********BARRES***********NOMBRES***********", lineno())
    print("\t", lineno(), "centre0_cercles :", centre0, "Maximum = 210")  # Point central des cercles-sections
    print("\t", lineno(), "centre1_barres :", centre1, "Maximum = 210")  # Point central des cercles-sections

    "# Cercles : Ø 420 | Rayon 210 |"
    int_sec = 210 / len(lis_sec)  # int_sec = Espace de déploiement des cercles-sections - Type float
    int_sec2 = 210 / int(t_tot)  # int_sec2 = Espace de déploiement des cercles-nombres - Type float
    (lineno(), "Cercles int_sec :", int_sec, "Total_nbr t_tot :", t_tot)
    tab_sec = [xy * int_sec for xy in range(1, len(lis_sec) + 1)]
    tab_sec2 = [xy * int_sec2 for xy in range(1, int(t_tot) + 1)]
    tab_sec.reverse()
    print(lineno(), "Cercles tab_sec :", tab_sec, "\n")  # Rayons des cercles des nombres
    # 486 Cercles tab_sec : [210.0, 183.75, 157.5, 131.25, 105.0, 78.75, 52.5, 26.25]

    "# Sections (barres) : Axes (y, x) (début et fin) | max_dro[bord_droit]"
    bord_gx, bord_gy = centre0[0] + 280, centre1[1] - 210
    bord_dx, bord_dy = max_dro, centre1[1] + 210
    # esp_x, esp_y = Espaces divisibles (nombres=sections=int(t_tot))3
    esp_x, esp_y = (bord_dx - bord_gx) // int(t_tot), (bord_dy - bord_gy) // int(t_tot)  # Lignes verticales
    esp_y1, esp_c = (bord_dy - bord_gy) // len(lis_sec), 0  # Lignes horizontales
    #
    rol_gx, rol_dx, rol_gy, rol_dy = bord_gx, bord_dx, bord_gy, bord_dy  # Horizontales
    rol_gx1, rol_dx1, rol_gy1, rol_dy1 = bord_gx, bord_dx, bord_gy, bord_dy  # Verticales
    dic_axe = {}  # Coordonnées (x, y) des nombres (clé.dic_axe)
    "# Trace les cercles-sections et les barres-nombres, en pointillés."
    for ts in tab_sec2:
        esp_c += 1
        if esp_c-1 < len(tab_sec):
            ms = tab_sec[esp_c-1]
            (lineno(), "esp_c :", esp_c, dico_gen[esp_c][1])
            # Lignes circulaires[rayons]
            cant.create_oval(centre0[0] - ms, centre0[1] - ms, centre0[0] + ms, centre0[1] + ms,
                             width=1, fill=o_color, dash=(1, 1), outline="orange")
            (lineno(), "Rayon ts :", ts, "esp_c :", esp_c, "Barres rol_gy :", rol_gy, "rol_gx1 :", rol_gx1)
            (lineno(), "ts :", ts)

        # Lignes horizontales[sections majeures] (divisibles par deux aux résultats pairs)
        nbr_gen = dico_gen[esp_c][1]
        if nbr_gen in tip_pai and len(tab_tip[nbr_gen]) > 1:
            n_pos = []
            for ng in tab_tip[nbr_gen]:
                n_dic = dic_taux[ng]
                n_pos.append(n_dic)
            n_long = len(n_pos)  # Nombre de fois - divisible par deux
            n_ind = dic_taux[nbr_gen][1]  # Section d'entrée maximale
            n_x, n_y = esp_x * (n_long - 1), esp_y1 * (n_long - 1)
            point1, point2 = (rol_gx1, rol_gy1), (rol_gx1, rol_gy1+(n_ind*esp_y1))
            point3, point4 = (rol_gx1 + n_x, rol_gy1+(n_ind*esp_y1) - n_y), (rol_gx1 + n_x, rol_gy1)
            cant.create_line(point1, point2, fill="purple", width=1, joinstyle=ROUND, capstyle=ROUND)
            cant.create_line(point2, point3, fill="purple", width=1, joinstyle=ROUND, capstyle=ROUND)
            cant.create_line(point3, point4, fill="purple", width=1, joinstyle=ROUND, capstyle=ROUND)
            cant.create_line(point1, point4, fill="purple", width=1, joinstyle=ROUND, capstyle=ROUND)
            cant.create_rectangle(point1, point3, fill="purple")
            (lineno(), "nbr_gen :", nbr_gen, "n_ind :", n_ind, "\t tab_tip :", tab_tip[nbr_gen], dic_taux[nbr_gen])
            (lineno(), "* Majeure esp_x :", esp_x, "\t esp_y1 :", esp_y1, "\t rol_gxy :", rol_gx1, rol_gy1)
            (lineno(), "n_long:", n_long, n_x, "x|y", n_y, "rol", rol_gx1, rol_gx1+n_x, rol_gy1, rol_gy1+n_y)
            (lineno(), " ")

        # Lignes horizontales[sections]
        if esp_c < len(lis_sec) + 2:
            # cant.create_line(rol_gx, rol_gy, rol_dx, rol_gy, width=1, fill='maroon', dash=(1, 1))  # Horizontales
            # rol_gy += esp_y1
            pass

        # Lignes verticales[nombres]
        "# Quand les nombres sont impairs inverser les poles des sections"
        # cant.create_line(rol_gx1, rol_gy1, rol_gx1, rol_dy1, width=1, fill='white', dash=(1, 1))  # Verticales
        (lineno(), "* * * * * Majeure rol_gy1 :", rol_gy1, "rol_dy1 :", rol_dy1)
        # 542 * * * * * Majeure rol_gy1 : 324 rol_dy1 : 744 # Constantes
        # Relevés ou topo
        dic_axe[nbr_gen] = ()
        if nbr_gen != 1:
            sec_deb, sec_fin = dic_taux[nbr_gen][1] - 1, dic_taux[nbr_gen][1]
            (lineno(), "nbr_gen :", nbr_gen, "sec_deb", sec_deb, "sec_fin", sec_fin)
            if dico_gen[esp_c][0][1] == 'pair':
                sec1xy, sec2xy = (rol_gx1, rol_gy1+(esp_y1*sec_deb)), (rol_gx1, rol_gy1+(esp_y1*sec_fin))  # Coord xy
                test = sec1xy[0], ((esp_y1 * float(dic_taux[nbr_gen][0])) / 100) + sec1xy[1]
                dic_axe[nbr_gen] = test
                (lineno(), "T1:", test, "\t secte.déb:", sec1xy, "secte.fin:", sec2xy, "T2:", dic_taux[nbr_gen])
                # 554 T1: 354.375 	 secte.déb: (527, 674) secte.fin: (527, 744) T2: ('6.25', 6)
                cant.create_line((rol_gx1, rol_gy1), sec2xy, width=1, fill="blue")  # Section entière
                cant.create_line(sec1xy, sec2xy, width=3, fill="blue")  # Section locale
                cant.create_line(test[0] - 5, test[1], test[0] + 5, test[1], width=3, fill="black")  # Section test
                (lineno(), '   pair nbr_gen :', nbr_gen, "test :", test)
            else:
                sec1xy, sec2xy = (rol_gx1, rol_dy1-(esp_y1*sec_deb)), (rol_gx1, rol_dy1-(esp_y1*sec_fin))  # Coord
                test = sec1xy[0], sec1xy[1] - ((esp_y1 * float(dic_taux[nbr_gen][0])) / 100)
                dic_axe[nbr_gen] = test
                (lineno(), "T1:", test, "\t secte.déb:", sec1xy, "secte.fin:", sec2xy, "T2:", dic_taux[nbr_gen])
                # 564 T1: (558, 459.625) 	 secte.déb: (558, 464) secte.fin: (558, 394) T2: ('6.25', 5)
                cant.create_line((rol_gx1, rol_dy1), sec2xy, width=1, fill="yellow")  # Section entière
                cant.create_line(sec1xy, sec2xy, width=3, fill="yellow")  # Section locale
                cant.create_line(test[0] - 5, test[1], test[0] + 5, test[1], width=3, fill="black")  # Section test
                (lineno(), '   impair nbr_gen :', nbr_gen)
            (lineno(), "nbr_gen :", nbr_gen, "sec_deb", sec_deb, "sec_fin", sec_fin)
        rol_gx1 += esp_x
    print(lineno(), "\n Les barres dic_axe :", dic_axe)
    (lineno(), "Verticales Barres : \tesp_x :", esp_x, "\tesp_y :", esp_y, "\tt_tot :", t_tot)
    (lineno(), "Horizontales Barres : \tesp_y1 :", esp_y1, "\tlis_sec :", len(lis_sec))
    (lineno(), "Intervalles Barres : \tesp_x*int :", esp_x * int(t_tot), "\tesp_y*int :", esp_y * int(t_tot))
    (lineno(), "Intervalles Barres : \tespace x :", bord_dx - bord_gx, "\tbords y :", bord_dy - bord_gy)
    (lineno(), "\ndic_taux:", dic_taux, "\ndico_gen :", dico_gen)

    # Lignes circulaires des rayons et section
    six0, sax0 = 60, []
    (lineno(), "six0:", six0)
    # 588 six0: 60
    for dtk, dtv in dic_taux.items():
        dtk6 = dtk % 6
        if dtk6 == 0:
            dtk6 = 6
        ray = ((int_sec * float(dtv[0])) // 100) + (int_sec * (int(dtv[1]) - 1))
        ang = dtk6 * six0
        (lineno(), "ray:", ray, "ang:", ang, "dtk:", dtk, "dtv:", dtv, "centre0:", centre0, "int_sec:", int_sec)
        x6 = ray * math.cos(math.radians(ang)) + centre0[0]
        y6 = ray * math.sin(math.radians(ang)) + centre0[1]
        xy6 = x6, y6
        if y6 > centre0[1]:  # centre0[1] = 534
            pos0 = (210 - (y6 - centre0[1]))
            (lineno(), "if y6:", y6, "pos0:", pos0, "dtk6:", dtk6)
        else:
            pos0 = ((centre0[1] - y6) - 210)
            (lineno(), "else y6:", y6, "pos0:", pos0, "dtk6:", dtk6)
        (lineno(), "xy6:", xy6, "dtk:", dtk, "dtk % 6:", dtk % 6)
        if dtk6 == 6:
            dtk6 = 0
        cant.create_line(centre0, xy6, fill=color6[dtk6], width=3)
        cant.create_line(xy6, dic_axe[dtk], fill=color6[dtk6], width=1)
        if dtk6 not in sax0:
            cant.create_line(xy6, (xy6[0], xy6[1] + pos0), fill=color6[dtk6], width=1)
            cant.create_text(xy6[0], xy6[1] + (pos0 + 6), text=str(dtk6), fill='black', font=c_ovale)
            sax0.append(dtk6)
    #

    print(c_ovale)
    print(lineno(), " Positions max_paires   max_dro", max_dro, "max-min", (max_dro - min_gau))
    print(lineno(), " Positions max impaires min_gau", min_gau)
    print(lineno(), " Positions bas_impaires lig_hau", lig_hau)


def traite(nombre):
    """Opération [n/2 ou n*3+1]."""
    '# Série : Cumulative des nombres précédents multipliés par deux [2, 4, 8, 16, 32, 64, 128,,,]'
    pro_deux, nbr_org = 2, nombre
    tab_deux.clear()
    tab_deux.append(pro_deux)
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
label = Label(debut, text='Entrez un nombre entier supérieur à 1')
label.pack()
final = Frame(root, width=1000, height=1000, bg='ivory')
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
